from bs4 import BeautifulSoup
import re
from nltk.metrics import distance
import csv

def remove_all_html_tags(text):
    soup = BeautifulSoup(text, features="html.parser")
    return soup.get_text()

def remove_all_special_chars(text):
    clean = re.sub(r'[^a-zA-Z0-9]', '', text)
    return clean


FILENAME = "words_part1.csv"
def get_recs(s: str) -> list[str]:
    rc = []
    with open(FILENAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for word in reader:
            d = distance.edit_distance(word[0].lower(), s.lower())
            rc.append((d, word[0]))
    rc.sort()
    return rc[:10]
