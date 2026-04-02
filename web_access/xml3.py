import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as ET
url = input("Enter url :")
html = urllib.request.urlopen(url).read()
tree = ET.fromstring(html)
cmt = tree.findall('comments/comment')
sum = 0
for i in cmt:
    count = i.find('count').text
    num = int(count)
    sum = sum + num
print(sum)