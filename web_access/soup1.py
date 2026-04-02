import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

url = input("Enter url : ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')
tag = soup('a')
print(tag)
for tags in tag:
    print(tags.get('href',None))