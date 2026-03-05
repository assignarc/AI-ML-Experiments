# Transformer-Based Movie Review Sentiment Analysis

> Same movie reviews but this time using actual transformers instead of just embeddings

## What's this?

Going back to movie review sentiment analysis but this time using **transformer models** instead of GloVe + Random Forest. Wanted to see how much better transformers actually are (spoiler: they're better).

## The problem

Still the same - predict if a movie review is positive or negative. But now using modern NLP with attention mechanisms.

## Data

**Movie Reviews** (`movie_reviews.csv`)

- Same movie review dataset as before
- Sentiment labels (positive/negative)

## What's different this time

Instead of:

- GloVe embeddings → averaging → Random Forest

Now using:

- **Sentence Transformers** - pre-trained transformer models
- Direct classification with transformer architectures
- Attention mechanisms to focus on important words

## Approach

1. **Load pre-trained transformer**
   - Using sentence-transformers library
   - Models like MiniLM, RoBERTa, etc.

2. **Get contextualized embeddings**
   - Unlike GloVe, these change based on context
   - "Bank" in "river bank" vs "bank account" get different vectors (finally!)

3. **Classification**
   - Either use transformer's built-in classification
   - Or use transformer embeddings + classifier

## What I'm learning

- Transformers capture context way better than static embeddings
- Pre-trained models are insanely good (transfer learning is real)
- Attention mechanisms let the model focus on relevant words
- Way better than GloVe for this task (but also heavier/slower)
- Using sentence-transformers is actually pretty easy

## Tech used

- **PyTorch** - deep learning framework
- **sentence-transformers** - pre-trained transformer models
- **Transformers** - attention mechanism architecture
- Same sklearn stuff for evaluation

## Files

- `Hands_on_Transformers_Notebook.ipynb` - transformer implementation
- `movie_reviews.csv` - movie review data

---

**Learned:** Transformers > embeddings. Context matters. Also, pre-trained models are magical.

[🔙 Back to W17](../) | [🔙 Back to Main](../../README.md)
