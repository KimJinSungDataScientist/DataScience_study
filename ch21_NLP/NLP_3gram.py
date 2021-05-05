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

triagram_transitions =defaultdict(list)
starts = []

for prev,current,next in zip (document,document[1:],document[2:]):
    # print(current)
    if prev==".":
        starts.append(current)

    triagram_transitions[(prev,current)].append(next)

# print(transitions)

import random

def generate_using_bigrams():
    current = random.choice(starts)
    prev = '.'
    result =[current]

    while True:
        next_word_candidates = triagram_transitions[(prev,current)]
        next_word = random.choice(next_word_candidates)

        prev, current = current,next_word
        result.append(current)
        if current =='.':
            return ' '.join(result)

print(generate_using_bigrams())
