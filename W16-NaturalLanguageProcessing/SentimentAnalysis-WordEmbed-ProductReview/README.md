# Product Review Sentiment Analysis

> Same idea as movie reviews but for products - turns out the approach is pretty similar

## What's this?

Another sentiment analysis project, this time for product reviews instead of movies. Using GloVe word embeddings to turn text into numbers, then training a classifier to figure out if customers are happy or not.

## The problem

Given a product review, is it **positive** or **negative**? Helps businesses understand what customers actually think (at scale, obviously).

## Data

**Product Reviews**

- Review text from various products
- Sentiment labels (positive/negative)

**GloVe Embeddings** - same 100-dimensional word vectors as before

## How it works

1. **Clean the text**
   - Remove HTML, special characters
   - Tokenize
   - Remove stopwords
   - Lemmatize

2. **Turn text into numbers**
   - Convert to GloVe word vectors
   - Average the embeddings for each review (simple but works)

3. **Classify**
   - Train ML model on vectorized reviews
   - Predict sentiment on new stuff

## What I used

- **Embeddings** - GloVe (Global Vectors)
- **NLP** - NLTK for preprocessing
- **Model** - Classification (RandomForest or similar)
- **Metrics** - Accuracy, precision, recall, F1

## What I learned

- Word embeddings work across different types of text (movies, products, whatever)
- Pre-trained embeddings generalize surprisingly well
- Text cleaning is still crucial (garbage in, garbage out)
- Averaging word vectors is basic but effective for representing sentences
- Product reviews have different patterns than movie reviews (interesting to see)

## Files

- `Product_Review_Sentiment_Analysis_Word_Embeddings.ipynb` - main notebook
- `Product_Reviews.csv` - product reviews
- `glove.6B.100d.txt` - GloVe embeddings (gitignored)
- `glove.6B.100d.txt.word2vec` - converted format for gensim

---

**Learned:** Same embedding approach works across domains. Also, people complain about products differently than movies.

[🔙 Back to W16](../) | [🔙 Back to Main](../../README.md)
