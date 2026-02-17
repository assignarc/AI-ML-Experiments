# Article Categorization

> Auto-categorizing news articles using word embeddings - actually works pretty well

## What's this?

Building a multi-class text classifier that sorts news articles into different topics. Using word embeddings to understand what articles are about, then Random Forest to do the heavy lifting.

## Why do this?

News sites get thousands of articles daily. Nobody's manually categorizing all that. This explores using NLP and ML to automate it.

**Real uses:**

- Recommendation engines
- Auto-tagging articles
- Personalized news feeds
- Keeping users engaged

## The problem

Given a news article, figure out which category it belongs to - politics, sports, tech, entertainment, business, etc. Multi-class classification (more than just yes/no).

## Data

**Articles Dataset**

- `Date published` - when it was published
- `Category` - what topic (this is what we're predicting)
- `Section` - article section
- `Headline` - the headline
- `Description` - article summary

Multiple categories to predict, so this is harder than binary classification.

## How I approached it

1. **Clean the text**
   - Remove HTML, weird characters
   - Tokenize
   - Remove stopwords
   - Lemmatize using NLTK

2. **Turn articles into vectors**
   - **GloVe embeddings** (100-dimensional)
   - Convert text to word vectors
   - Average them to get document vectors (simple but works)

3. **Train the model**
   - **Random Forest** for multi-class
   - Check feature importance

4. **See how it did**
   - Accuracy, Precision, Recall, F1
   - Confusion matrix to see where it messes up
   - Classification report

## Techniques

- **Word Embeddings** - GloVe
- **NLP** - NLTK for preprocessing, gensim for embeddings
- **Model** - Random Forest (handles multi-class well)
- **Text Processing** - tokenization, lemmatization, stopword removal

## What I figured out

- Word embeddings work great for multi-class text stuff
- Random Forest surprisingly handles high-dimensional embedding features well
- Pre-trained GloVe saves so much time (no need to train from scratch)
- Text preprocessing (especially lemmatization) makes a real difference
- Different article categories have pretty distinct word patterns (makes sense when you think about it)
- Averaging word vectors is simple but actually effective for documents

## Files

- `Articles_Categorization.ipynb` - main notebook
- `Articles.csv` - news articles (~23 MB)
- `glove.6B.100d.txt` - GloVe embeddings (331 MB, gitignored)
- `glove.6B.100d.txt.word2vec` - gensim format

---

**Learned:** Multi-class classification is trickier than binary, but same embedding approach works. Pre-trained embeddings are a lifesaver.

[🔙 Back to W16](../) | [🔙 Back to Main](../../README.md)
