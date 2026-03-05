# 📝 Natural Language Processing (W16)

> **Learning Module:** Tokenizing, stemming, and vectorizing raw text to make ML models actually understand human language.

---

## What's this about?

This week is entirely focused on turning unstructured text (like movie reviews, tweets, or articles) into numbers so that a machine learning model can actually work with it. 

### The Goal

We can't just pass the string "I loved this movie" into a Random Forest. The goal here is to:

- Clean text data (removing stopwords, punctuation).
- Break sentences down into their root words.
- Use vectorization techniques (Bag of Words, TF-IDF) to represent those words as matrices.
- Train predictive models on those numeric representations.

---

## The Data

**Format:** Usually raw CSVs loaded with text strings (like IMDB reviews).

### Typical Vectorization Metrics

| Technique | Description | Pros/Cons |
| ----------------------- | -------------------------------- | ----------- |
| Stopword Removal | Stripping words like "the", "a", "is" | Shrinks vocabulary massively |
| Stemming | Chopping off ends of words (running -> run) | Fast, but sometimes makes fake words |
| Lemmatization | Finding the dictionary root | Slower but accurate |
| CountVectorizer | Bag of words (how many times a word appears) | Very large sparse matrices |
| TF-IDF | Term Frequency-Inverse Document Frequency | Weighs unique "important" words higher |

---

## What I'm trying to do

### 1. Text Preprocessing Pipeline

- Use NLTK/Spacy to completely clean the text.
- Remove HTML tags if scraping from the web.

### 2. Feature Engineering

- Fit a `TfidfVectorizer` to scale down the noise of common words.
- Explore n-grams (grouping words like "not good" instead of just "not" and "good").

### 3. Classification

- Feed the TF-IDF matrix into a Naive Bayes or Logistic Regression model to predict sentiment.

---

## Quick Numbers

Preprocessing text drastically reduces the dimensions of your dataset. Going through a corpus of 10,000 sentences with raw vocab might yield 50,000 features. Applying stemming and TF-IDF can cut that in half, vastly speeding up model training (GridSearch is slow but worth it).

---

## Tech Stack
### Packages Needed For This Module:
- `gensim`
- `matplotlib`
- `nltk`
- `numpy`
- `pandas`
- `seaborn`
- `sklearn`
- `string`


- **Python 3.8+**
- **NLTK (Natural Language Toolkit)** - The gold standard for text processing
- **Spacy** - Also highly used for advanced NLP
- **Scikit-learn** - For TF-IDF and count vectorization
- **Pandas / NumPy**

---

## What I Learned

- Text processing is 90% of the work in NLP (there is always messy data everywhere).
- N-grams are huge. If a review says "this movie was not good", unigrams count "good" as a positive word, which ruins the prediction!
- TF-IDF almost always outperforms simple Bag of Words because it punishes words that appear too often.

---

## 🔗 Links

- [Back to Main Repository](../)
- [P4: Medical Diagnosis (RAG Example)](../P4-MedicalDiagnosis)

---

**Project Date:** 2024  
**Domain:** Natural Language Processing (NLP)
