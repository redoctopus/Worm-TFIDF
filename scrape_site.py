"""
Worm TFIDF -- Site Scraper
jocelynh
---
Scrapes the parahumans.wordpress.com site for each chapter.
"""
import re
import requests

from bs4 import BeautifulSoup as bs

FIRST_PAGE = 'https://parahumans.wordpress.com/category/stories-arcs-1-10/arc-1-gestation/1-01/'

def next_chapter_in_text(tag):
    """
    Returns True if the text of the tag contains "Next Chapter".
    We need this because there's a bit of variation in the text of the 
    <a href= ...> tag, so we can't just use find(string="Next Chapter").
    """
    if (tag.name == 'a' and
            tag.string != None and
            'next chapter' in tag.string.lower()):
        return True
    return False


def scrape_worm(start_link=FIRST_PAGE, maximum=None):
    """
    Scrapes every chapter, starting from the link given if provided.

    Returns a list of tuples: [(chapter_title, [list of words]), ...], as well 
    as the dictionary as a set.
    (List and not dict because we want these in chapter order.)
    """
    link = start_link
    count = 0
    chapter_words = []
    D = set()

    # Keep scraping until the "Next Chapter" link is just "End"
    while(link != None):
        response = requests.get(link, timeout=10)
        content = bs(response.content, 'html.parser')
        
        # Find title of the chapter
        title = content.find(class_='entry-title').string
        print(title)

        # Find next link
        next_chapter_tag = content.find(next_chapter_in_text)
        if next_chapter_tag != None:
            link = next_chapter_tag.get('href')
        else:
            link = None

        # Chapter content
        chapter_text_tags = content.find_all('p')
        chapter_text = []
        # Remove non alphabet characters, split into words
        for paragraph in chapter_text_tags[1:]:
            paragraph = paragraph.get_text()
            paragraph = re.sub(r'-', ' ', paragraph)
            paragraph = re.sub(r'[^a-zA-Z\s]+', '', paragraph)
            if 'Next Chapter' in paragraph or 'Last Chapter' in paragraph:
                break
            words = [w.lower() for w in paragraph.split()]
            chapter_text += words

        chapter_words.append((title, chapter_text))
        D |= set(chapter_text)

        count += 1
        if maximum != None and count >= maximum:
            break
    
    return chapter_words, D

if __name__ == '__main__':
    # Start off in Gestation 1.1
    chapter_words = scrape_worm()
    chapter_dict = dict(chapter_words)

