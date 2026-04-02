import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
start_url  = input('Enter url : ')
current_url = start_url
counts = int(input('Enter counts:'))
position = int(input('Enter position :'))
while counts>0:
    html = urllib.request.urlopen(current_url,context = ctx).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    links = list()
    for tag in tags:
        link = tag.get('href',None)
        links.append(link)
    current_url = links[position-1]
    counts = counts - 1
    print('Retrieving:',current_url)
    
