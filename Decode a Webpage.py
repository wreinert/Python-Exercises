#Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
import requests
from bs4 import BeautifulSoup

base_url = 'https://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, features="html.parser")
classa = "css-xxaj7r"
titles = []

for classa in soup.find_all(class_="css-xxaj7r"):
    titles.append(classa.next_element.next_element)
    #print(classa.next_element.next_element)
print(titles)


