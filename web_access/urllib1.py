import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
links= list()
x = 0
url = input('Enter url :')
def link(url):
    #counts = counts + 1
    html = urllib.request.urlopen(url,context = ctx).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    for tag in tags:
        t = tag.get('href',None)
        links.append(t)
link(url)
while counts<3:
    y = 2 + x
    link(links[y])
    counts = counts + 1
    x = x + 100
    print()
#link(url)
print(len(links))

print(len(links))
