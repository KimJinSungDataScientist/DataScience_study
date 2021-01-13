from bs4 import BeautifulSoup
import requests

url = "https://www.house.gov/representatives"
text = requests.get(url).text
soup = BeautifulSoup(text,"html5lib")

all_urls = [a['href']
            for a in soup('a')
            if a.has_attr('href')]

print(len(all_urls))

import re

regex = r"^https?://.*\.house\.gov/?$"

good_urls = [url for url in all_urls if re.match(regex,url)]
print(len(good_urls))

good_urls = list(set(good_urls))
print(len(good_urls))

html = requests.get('https://jayapal.house.gov').text
soup = BeautifulSoup(html,'html5lib')

links = {a['href'] for a in soup('a') if 'press releases' in a.text.lower()}

print(links)

from typing import Dict, Set

press_releases: Dict[str, Set[str]]= {}

#for house_url in good_urls:
    #html = requests.get(house_url).text
    #soup = BeautifulSoup(html,'html5lib')
    #pr_links = {a['href'] for a in soup('a') if 'press releases' in a.text.lower()}
    #print(f"{house_url}: {pr_links}")
    #press_releases[house_url] = pr_links


def paragraph_mentions(text, keyword):
    soup = BeautifulSoup(text,'html5lib')
    paragraphs = [p.get_text() for p in soup('p')]

    return any(keyword.lower() in paragraph.lower()
               for paragraph in paragraphs)

text = """<body><h1>Facebook</h1><p>Twitter</p>"""
print(paragraph_mentions(text,"twitter"))

for house_url, pr_links in press_releases.items():
    for pr_link in pr_links:
        url = f"{house_url}/{pr_link}"
        text = requests.get(url).text
        if paragraph_mentions(text,'data'):
            print(f"{house_url}")
            break

            #10.4 정제하고 합치기
            #이것이 데이터분석이다 ~2.2 나무위키
            #