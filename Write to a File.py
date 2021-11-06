#Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code, use the code from the solution),
# and instead of printing the results to a screen, write the results to a txt file.
#In your code, just make up a name for the file you are saving to.
#Extras: Ask the user to specify the name of the output file that will be saved.

import requests
from bs4 import BeautifulSoup
import json

base_url = 'https://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, features="html.parser")
classa = "css-xxaj7r"
titles = []

for classa in soup.find_all(class_="css-xxaj7r"):
    titles.append(classa.next_element.next_element)
    #print(classa.next_element.next_element)
#print(titles)

with open('write_to_a_file.txt', 'w') as open_file:
    open_file.write(', '.join(titles))


