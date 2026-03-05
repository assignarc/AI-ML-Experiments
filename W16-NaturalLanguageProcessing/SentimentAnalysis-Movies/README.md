# Movie Review Sentiment Analysis

> Figuring out if movie reviews are thumbs up or thumbs down using word embeddings

## What's this?

Built a sentiment analysis thing for movie reviews. Instead of just counting words (bag-of-words is pretty basic), used GloVe word embeddings to actually understand what words mean. Then threw it at a Random Forest to classify positive vs negative reviews.

## The problem

Given a movie review, predict if it's **positive** or **negative**. Classic NLP stuff.

## Data

**Movie Reviews**

- `review` - the actual review text
- `sentiment` - 0 = negative, 1 = positive

Also using **GloVe embeddings** (`glove.6B.100d.txt`) - these are pre-trained word vectors that somehow capture word relationships (pretty neat actually).

## How I did it

1. **Cleaning the text**
   - Lowercase everything
   - Strip HTML tags (some reviews had them)
   - Tokenize into words
   - Remove stopwords (the, is, and, etc.)
   - Lemmatize (convert words to base form)

2. **Word Embeddings**
   - Used GloVe (100-dimensional vectors)
   - Way better than just counting words

3. **Model**
   - Random Forest Classifier
   - Trained on the word vectors

## Results

- **Train:** ~84%
- **Test:** ~81%

Not bad! Model doesn't overfit too much which is good.

## What I learned

- Word embeddings are way better than bag-of-words (duh)
- GloVe vectors actually capture semantic similarity - words with similar meanings are close together
- Text preprocessing matters more than I thought (lemmatization helps a lot)
- Random Forest handles high-dimensional stuff pretty well
- Pre-trained embeddings are a huge time saver (no need to train your own)

## What I used

- **NLP stuff** - NLTK for tokenization, stopwords, lemmatization
- **Embeddings** - GloVe pre-trained vectors
- **Model** - Random Forest
- **Libraries** - NLTK, sklearn, gensim

## Files

- `Sentiment_Analysis_Hands_on.ipynb` - main notebook
- `movie_reviews.csv` - reviews dataset
- `glove.6B.100d.txt` - GloVe embeddings (331 MB, ignored in git)

---

**Learned:** Word embeddings > counting words. Also, text preprocessing is annoying but necessary.

[🔙 Back to W16](../) | [🔙 Back to Main](../../README.md)
