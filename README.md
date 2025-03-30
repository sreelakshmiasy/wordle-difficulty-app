# Wordle Difficulty Predictor

This project predicts how difficult a Wordle word might be based on its features such as letter frequency, number of vowels, presence of rare letters, and more.

## Project Goals

- Analyze the Wordle answer list
- Extract features like letter rarity, frequency, vowel count, etc.
- Assign a difficulty label (Easy, Medium, Hard)
- Build an ML model to predict difficulty based on these features
- Deploy as a web app using Streamlit

## Dataset

The original Wordle word list was sourced from [tabatkins/wordle-list](https://github.com/tabatkins/wordle-list).

Word frequency data was obtained using the [wordfreq Python package](https://github.com/rspeer/wordfreq), which is based on large English corpora.

## Project Status

- [x] Word list imported
- [x] Word frequency added
- [x] Feature engineering done
- [ ] ML model training
- [ ] Evaluation and interpretation
- [ ] Optional deployment

## Future Ideas

- Train a classifier using Random Forest or XGBoost
- Add real-world guess statistics (from Reddit, Twitter, or simulated guesses)
- Deploy a Wordle difficulty predictor as a web app
