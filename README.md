# 🧩 How Hard Was Today’s Wordle Word?

An interactive machine learning app that predicts how difficult a 5-letter Wordle word is, explains the prediction with SHAP, and lets users explore word patterns, difficulty levels, and insights — all in one place.

👉 **Try it live:**  
🔗 [https://wordle-difficulty.streamlit.app](https://wordle-difficulty.streamlit.app)

---

## 🚀 Features

✅ Predicts difficulty level (Easy / Medium / Hard) for any 5-letter word  
✅ Interactive feedback: *“Did you guess the word?”*  
✅ SHAP waterfall plots to explain the prediction  
✅ Feature breakdown table for each word  
✅ Live word search by letter patterns  
✅ Dataset explorer: filter by difficulty, sort by frequency/vowels  
✅ Built with Streamlit, scikit-learn, SHAP, and Python

---

## 📁 Project Structure

```
wordle-difficulty-predictor/
│
├── app.py                      # Streamlit app
├── wordle_model.pkl            # Trained RandomForestClassifier
├── X_columns.pkl               # Feature columns used in training
├── wordfreq_features.py       # Feature extraction code
├── wordle_difficulty_data.csv # Dataset with difficulty labels
├── requirements.txt            # App dependencies
└── notebooks/
    ├── 01_Data_Exploration.ipynb
    └── 03_SHAP_Explainability.ipynb
```

---

## 🧠 ML & Features

The model uses:
- **Word frequency** in English
- **Vowel count**
- **Rare letter count** (e.g., q, z, x, j, k)
- **Duplicate letters**

It classifies difficulty into:
- `Easy`
- `Medium`
- `Hard`

With **SHAP explainability** to interpret predictions.

---

## 🛠️ Run Locally

### 1. Clone this repo
```bash
git clone https://github.com/sreelakshmiasy/wordle-difficulty-predictor.git
cd wordle-difficulty-predictor
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py
```

---

## 📚 Notebooks Included

- `01_Data_Exploration.ipynb` — Load and explore the dataset  
- `03_SHAP_Explainability.ipynb` — Visualize SHAP explanations for sample predictions

---

## ✨ Inspiration

Inspired by the relatable question we all ask while playing Wordle:
> *“Was it just me, or was that word actually hard?”*

Now you can find out — with explainable AI. 😄

---

## 👩‍💻 Author

**Sreelakshmi Asy**  
🔗 [GitHub](https://github.com/sreelakshmiasy)  
🔗 [LinkedIn](https://www.linkedin.com/in/sreelaxmias/)
---


