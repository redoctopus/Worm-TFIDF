"""
Worm TFIDF -- tf-idf Implementation
jocelynh
---
Implements tf-idf.
"""
from scrape_site import scrape_worm

if __name__ == '__main__':
    chapter_words, D = scrape_worm(maximum=7)
    chapter_dict = dict(chapter_words)

