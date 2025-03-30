import streamlit as st
import pickle
import pandas as pd
import shap
import numpy as np
import matplotlib.pyplot as plt

from wordfreq_features import extract_features_from_word

#Page config
st.set_page_config(page_title="How hard was today's Wordle word?", page_icon="🧩")

#Load model and feature columns
model = pickle.load(open("wordle_model.pkl", "rb"))
X_columns = pickle.load(open("X_columns.pkl", "rb"))
explainer = shap.Explainer(model)

#Load dataset
@st.cache_data
def load_wordle_data():
    return pd.read_csv("wordle_difficulty_data.csv")

df_words = load_wordle_data()

#Title
st.title("🧩 How hard was today's Wordle word?")

#Input
word = st.text_input("Enter the 5-letter Wordle word:")

if word:
    word = word.lower().strip()

    if len(word) != 5 or not word.isalpha():
        st.error("🚫 Please enter a valid 5-letter word.")
    else:
        #Feature engineering
        features = extract_features_from_word(word)
        X = pd.DataFrame([features])[X_columns]

        #Predict
        pred_class = model.predict(X)[0]
        st.success(f"🧠 It's **{pred_class}**!")

        #User guess input
        st.subheader("🤔 Did you guess the word correctly?")
        user_guess = st.radio("Your answer:", ["Yes", "No"], index=None)

        #Respond based on combo ONLY if user selects an option
        if user_guess:
            if user_guess == "Yes":
                if pred_class == "Hard":
                    st.success("🎉 Wow, you're a genius!")
                else:
                    st.success("🎉 Yay! You did it!")
            else:  # user_guess == "No"
                if pred_class == "Hard":
                    st.info("😮 Yeah...makes sense, it was hard!")
                else:
                    st.info("😅 We all have that day! But there's always tomorrow :)")

        
        #SHAP waterfall plot
        st.markdown(f"## 🧩 But why is it **{pred_class}**?")
        st.subheader("📊 Feature Impact (SHAP Explanation)")
        shap_values = explainer(X)
        class_index = list(model.classes_).index(pred_class)
        fig, ax = plt.subplots()
        shap.plots.waterfall(shap_values[0, :, class_index], show=False)
        st.pyplot(fig)


        #Feature breakdown
        st.markdown("### 🧩 Feature Breakdown")
        feat_df = pd.DataFrame([features]).T.rename(columns={0: "Value"})
        feat_df.index.name = "Feature"
        st.table(feat_df)

#Dataset Explorer
st.markdown("## 📚 Explore Word Dataset")

#Column info
st.markdown("### ℹ️ What the columns mean:")
st.markdown("""
- **word**: The 5-letter word itself  
- **frequency**: How commonly the word is used in English (wordfreq score)  
- **vowel_count**: Number of vowels in the word (a, e, i, o, u)  
- **rare_letter_count**: Number of rare letters (q, z, x, j, k)  
- **has_duplicates**: 1 if the word has repeated letters, 0 otherwise  
- **difficulty**: The labeled difficulty of the word (Easy / Medium / Hard)
""")

#Filter by difficulty
selected_difficulty = st.selectbox(
    "Filter words by difficulty:",
    ["All", "Easy", "Medium", "Hard"]
)

if selected_difficulty == "All":
    filtered_df = df_words.copy()
else:
    filtered_df = df_words[df_words["difficulty"] == selected_difficulty]

#Sorting
sort_column = st.selectbox(
    "Sort by column:",
    ["None", "frequency", "vowel_count"]
)

sort_order = st.radio(
    "Sort order:",
    ["Descending", "Ascending"],
    horizontal=True
)

if sort_column != "None":
    ascending = True if sort_order == "Ascending" else False
    filtered_df = filtered_df.sort_values(by=sort_column, ascending=ascending)

#Show table
st.dataframe(filtered_df.reset_index(drop=True), use_container_width=True)

#Live Pattern-Based Word Search
st.markdown("## 🔠 Live Word Search by Letter Pattern")
st.caption("Type continuously to see matching words update live")

live_pattern = st.text_input("Type any number of letters (e.g., 'a', 'ou', 'ing'):") 

if live_pattern:
    live_pattern = live_pattern.lower().strip()

    if not live_pattern.isalpha():
        st.warning("⚠️ Please enter only alphabetic characters.")
    else:
        live_matches = df_words[df_words["word"].str.contains(live_pattern)]
        st.write(f"🔎 Words containing '{live_pattern}' in order: {len(live_matches)} found")
        st.dataframe(live_matches.reset_index(drop=True), use_container_width=True)
