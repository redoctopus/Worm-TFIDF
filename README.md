# Worm-TFIDF
A small side project to maybe find some interesting word usage patterns in the web serial [Worm](https://parahumans.wordpress.com/).

There's some inexactness because of my naive filtering (accent marks are not processed correctly), but that shouldn't affect anything too much. I may or may not come back and fix it.

## TF-IDF
Stands for term frequency-inverse document frequency. In short, it's a way to measure how important a word is to a particular document (in this case, a chapter) relative to the whole corpus (in this case, all of Worm).

Term frequency is calculated given a word and a document, such that `tf(w,d) = (# of times w appears in d)`.

Inverse document frequency is calculated given a word, such that `idf(w) = log(# of documents/# documents containing w)`.

Then, `tfidf(w,d) = tf(w,d) * idf(w)`. Words with the higher tf-idf scores per chapter are ones that appear proportionally more in that chapter than in the rest of Worm.

## Results
For the tf-idf results per chapter, computed over the full corpus, click [here](results/results_full_corpus.txt).
