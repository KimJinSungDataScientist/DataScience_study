def fix_unicode(text: str)->str:
    return text.replace(u"\u2019","'")

import re
from bs4 import BeautifulSoup
import requests

url = 'https://www.oreilly.com/ideas/what-is-data-science'
html = requests.get(url).text
soup=BeautifulSoup(html, 'html5lib')

content=soup.find('div','main-post-radar-content')
regex=r"[\w']+|[\.]"

document = []

for paragraph in content('p'):
    words = re.findall(regex,fix_unicode(paragraph.text))
    document.extend(words)

# print(document)


from collections import defaultdict

transitions =defaultdict(list)
for prev,current in zip (document,document[1:]):
    # print(current)
    transitions[prev].append(current)

# print(transitions)

import random

def generate_using_bigrams():
    current = '.'
    result =[]
    while True:
        next_word_candidates = transitions[current]
        current = random.choice(next_word_candidates)
        result.append(current)
        if current =='.':
            return ' '.join(result)

print(generate_using_bigrams())
