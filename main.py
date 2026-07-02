#to run the venv in terminal: "source venv/bin/activate"

import requests
import re

def format_undersc(text):
    text_words = text.split(" ")
    return "_".join(text_words)

def get_article(title):
    title_argument = format_undersc(title)
    url = f"https://en.wikipedia.org/w/index.php?title={title_argument}&action=raw" 
    response = requests.get(url, headers={"user-agent":"curl/8.5.0"})
    return response.text

def get_links(article_text):
    word_pattern = re.compile(r"\[\[([\w\s]+)\]\]")
    list_links = word_pattern.findall(article_text)
    return list_links

def get_links_urls(linkslist):
    list_urls = []
    for link in linkslist:
        list_urls.append(f"https://en.wikipedia.org/wiki/{format_undersc(link)}")
    return list_urls

def get_single_url(title):
    return f"https://en.wikipedia.org/wiki/{format_undersc(title)}"


if __name__ == '__main__':
    x = input("prompt: ")
    wiki_mush = get_article(x)
    print(sorted(get_links(wiki_mush)))
    print(f"https://en.wikipedia.org/wiki/{format_undersc(x)}")
