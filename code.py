import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

base_url= 'https://www.nytimes.com/'
r=requests.get(base_url)
soup=BeautifulSoup(urlopen(base_url), features='lxml')

get_titles=soup.find_all(class_="css-1j836f9 esl82me3" )

print()
for title in get_titles:
    print(title.text)
