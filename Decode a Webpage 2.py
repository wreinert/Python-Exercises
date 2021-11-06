#Using the requests and BeautifulSoup Python libraries,
# print to the screen the full text of the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

import requests
from bs4 import BeautifulSoup

base_url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, features="html.parser")

print(soup.get_text())



