from bs4 import BeautifulSoup
import re


def remove_all_html_tags(text):
    soup = BeautifulSoup(text, features="html.parser")
    return soup.get_text()

def remove_all_special_chars(text):
    clean = re.sub(r'[^a-zA-Z0-9]', '', text)
    return clean
