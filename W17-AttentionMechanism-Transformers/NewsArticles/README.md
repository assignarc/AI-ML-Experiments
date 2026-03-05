# News Article Categorization with Transformers

> Article classification but this time using transformers to see if they're actually better

## What's this?

Multi-class text classification for news articles using **transformers and attention mechanisms**. Testing if transformer models beat the GloVe + Random Forest approach from before.

## The problem

Given a news article, categorize it into the right topic (politics, sports, tech, business, etc.). Same as before but with better models.

## Data

**News Articles**

- `news_articles.csv` - article text
- `news_article_labels.csv` - category labels
- Multiple categories (multi-class problem)

## New approach

**Before (W16):**

- GloVe embeddings
- Average word vectors
- Random Forest

**Now (W17):**

- **Sentence transformers** - contextualized embeddings
- Attention mechanisms to focus on important parts
- Better handling of document-level semantics

## How it works

1. **Use pre-trained transformers**
   - sentence-transformers models
   - Already trained on tons of text
   - Understand context and semantics

2. **Get document embeddings**
   - Transformers create sentence/document vectors
   - Capture context better than averaging GloVe

3. **Multi-class classification**
   - Fine-tune transformer or use embeddings
   - Classify into article categories

## What I'm learning

- Transformers handle longer documents better
- Attention lets model focus on key phrases
- Pre-trained transformers already "understand" topics pretty well
- Transfer learning saves so much time (and compute)
- Multi-class with transformers is actually straightforward
- sentence-transformers library makes this way easier than expected

## Tech used

- **PyTorch** (`torch`) - deep learning
- **sentence-transformers** - pre-trained models
- Attention mechanisms
- sklearn for metrics

## Files

- `News_Article_Categorization_Notebook.ipynb` - main implementation
- `news_articles.csv` - article data
- `news_article_labels.csv` - category labels

---

**Learned:** Transformers are better for longer text. Context > word counts. Pre-training is OP.

[🔙 Back to W17](../) | [🔙 Back to Main](../../README.md)
