# coding: utf-8

import re
import sys
import urllib
import urllib.request
from requests import get
from urllib.request import urlopen
from bs4 import BeautifulSoup

## Filtering text

r = get('https://experts.illinois.edu/en/publications/pore-scale-simulation-of-biomass-growth-along-the-transverse-mixi')
soup = BeautifulSoup(r.content.decode('utf-8'), 'html.parser')
#print(soup)
# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out
# get text
text = soup.get_text()
# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)
#print(text)
#print(type(text))
#print(len(text))

file = open('paper_data.txt', 'w')
file.write(text)
file.write('\n')
file.flush()
file.close()

txt = open("paper_data.txt", "r")
s=txt.readlines()
str1 = ''.join(s)
print(str1)

print(str1.find('Abstract'))
print(str1.find('Original'))
abstract_clean = str1[571:2261]
print(abstract_clean)

file = open('abstract_clean.txt', 'w')
file.write(abstract_clean)
file.write('\n')
file.flush()
file.close()