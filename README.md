# Worm-TFIDF
A small side project to maybe find some interesting word importance patterns in the web serial [Worm](https://parahumans.wordpress.com/).

Results over the full corpus are [here](results/results_full_corpus.txt).

There's some inexactness because of my naive filtering (accent marks are not processed correctly), but that shouldn't affect anything too much. I may or may not come back and fix it.

May contain spoilers for Worm.

## TF-IDF
Stands for term frequency-inverse document frequency. In short, it's a way to measure how important a word is to a particular document (in this case, a chapter) relative to the whole corpus (in this case, all of Worm).

As an example, a few of the words with the highest tf-idf scores for the very first chapter, Gestation 1.1, are "madison,", "juice," "lunch," "mr," and "gladly." On the other hand, the words with the highest tf-idf scores for Gestation 1.6 (when Armsmaster first shows up) are "armsmaster," "credit," "capture," "east," and "lung."

### Slightly More Technical Details
Term frequency is calculated given a word and a document, such that `tf(w,d) = (# of times w appears in d)`.

Inverse document frequency is calculated given a word, such that `idf(w) = log(# of documents/# documents containing w)`.

Then, `tfidf(w,d) = tf(w,d) * idf(w)`.

Words with the higher tf-idf scores per chapter are ones that appear proportionally more in that chapter than in the rest of Worm. This also conveniently means that words that are common across all chapters, such as stopwords (e.g. as, of, a, and, etc.) are naturally lower in the heirarchy and don't make it into the top 10.

## Results
For the tf-idf results per chapter, computed over the full corpus (such that each chapter is compared to every other chapter in Worm), [click here](results/results_full_corpus.txt).

Results of running on individual arcs (such that each chapter is only compared to other chapters in the same arc):
1. [Gestation](results/results_arc_01.txt)
1. [Insinuation](results/results_arc_02.txt)
1. [Agitation](results/results_arc_03.txt)
1. [Shell](results/results_arc_04.txt)
1. [Hive](results/results_arc_05.txt)
1. [Tangle](results/results_arc_06.txt)
1. [Buzz](results/results_arc_07.txt)
1. [Extermination](results/results_arc_08.txt)
1. [Sentinel](results/results_arc_09.txt)
1. [Parasite](results/results_arc_10.txt)
1. [Infestation](results/results_arc_11.txt)
1. [Plague](results/results_arc_12.txt)
1. [Snare](results/results_arc_13.txt)
1. [Prey](results/results_arc_14.txt)
1. [Colony](results/results_arc_15.txt)
1. [Monarch](results/results_arc_16.txt)
1. [Migration](results/results_arc_17.txt)
1. [Queen](results/results_arc_18.txt)
1. [Scourge](results/results_arc_19.txt)
1. [Chrysalis](results/results_arc_20.txt)
1. [Imago](results/results_arc_21.txt)
1. [Cell](results/results_arc_22.txt)
1. [Drone](results/results_arc_23.txt)
1. [Crushed](results/results_arc_24.txt)
1. [Scarab](results/results_arc_25.txt)
1. [Sting](results/results_arc_26.txt)
1. [Extinction](results/results_arc_27.txt)
1. [Cockroaches](results/results_arc_28.txt)
1. [Venom](results/results_arc_29.txt)
1. [Speck](results/results_arc_30.txt)
1. [Epilogue: Teneral](results/results_arc_31.txt)
