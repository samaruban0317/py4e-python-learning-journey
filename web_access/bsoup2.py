import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url : ')
html = urllib.request.urlopen(url,context=ctx).read()

soup = BeautifulSoup(html,'html.parser')
tags = soup('span')

numbers = list()
for tag in tags:
    nums = tag.contents[0]
    numbers.append(nums)

counts = 0
for num in numbers:
    n = int(num)
    counts = counts + n
print(counts) 