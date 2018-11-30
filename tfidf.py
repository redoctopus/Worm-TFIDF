"""
Worm TFIDF -- tf-idf Implementation
jocelynh
---
Implements tf-idf.

tf(word, doc) = # of times word appears in doc
idf(word) = log[(# of documents in which word appears)/(# docs total)]

tfidf(word, doc) = tf(word, doc)*idf(word)

So for a given document (in this case, a chapter), a word w with high 
tfidf(w, d) means that it appears proportionally higher in d than elsewhere 
in the corpus (i.e. Worm).
"""
import argparse
import math
from collections import Counter

from scrape_site import scrape_worm

parser = argparse.ArgumentParser(description="TF-IDF analysis of Worm.")
parser.add_argument('--arc', '-a', type=int, default=0,
        help="Which arc to examine. If none given, crawls all of Worm.")

scrape_params = [
        ('2011/06/11/1-1/', None),
        ('2011/06/11/1-1/', 7),
        ('2011/07/05/insinuation-2-1/', 10),
        ('2011/08/09/agitation-3-1/', 13),
        ('2011/09/24/shell-4-1/', 13),
        ('2011/11/05/hive-5-1/', 11),
        ('2011/12/13/tangle-6-1/', 10),
        ('2012/01/17/buzz-7-1/', 13),
        ('2012/03/03/extermination-8-1/', 10),
        ('2012/04/03/cell-9-1/', 6),
        ('2012/04/24/parasite-10-1/', 8),
        ('2012/05/19/infestation-11-1/', 16),
        ('2012/06/26/plague-12-1/', 10),
        ('2012/07/28/snare-13-1/', 12),
        ('2012/09/04/prey-14-1/', 13),
        ('2012/10/16/colony-15-1/', 14),
        ('2012/11/24/monarch-16-1/', 16),
        ('2013/01/08/migration-17-1/', 8),
        ('2013/01/19/queen-18-1/', 13),
        ('2013/02/19/scourge-19-1/', 10),
        ('2013/03/21/chrysalis-20-1/', 7),
        ('2013/04/09/imago-21-1/', 9),
        ('2013/05/04/cell-22-1/', 8),
        ('2013/05/25/drone-23-1/', 6),
        ('2013/06/08/crushed-24-1/', 7),
        ('2013/06/29/scarab-25-1/', 7),
        ('2013/07/18/sting-26-1/', 10),
        ('2013/08/13/extinction-27-1/', 7),
        ('2013/08/31/cockroaches-28-1/', 7),
        ('2013/09/19/venom-29-1/', 10),
        ('2013/10/15/speck-30-1/', 7),
        ('2013/11/02/teneral-e-1/', 6)
        ]

if __name__ == '__main__':
    # Note: document frequencies calculated in scrape_worm().
    base = 'https://parahumans.wordpress.com/'
    args = parser.parse_args()
    arc = args.arc

    #TODO: Use whole arcs as documents someday?

    if arc in range(32): # 0 scrapes everything
        start, maximum = scrape_params[arc]
        chapter_words, N, dfs = scrape_worm(
            start_link=base+start, maximum=maximum)
    else:
        print("There are only 31 arcs (including the epilogue)!")

    chapter_dict = dict(chapter_words)

    for (title, words) in chapter_words:
        tfs = Counter(words)    # Gives {"w1": (# of w1), "w2": (# of w2), ...}
        tfidfs = []
        for w in tfs.keys():
            tfidf = tfs[w] * math.log(N*1./dfs[w])
            tfidfs.append((w, tfidf))

        tfidfs.sort(key=lambda x: x[1], reverse=True)
        print("====")
        print(title)
        for (w,tfidf) in tfidfs[:10]:
            print(w+": "+str(round(tfidf,2)), end=", ")
        print("\n")
