import urllib.request,urllib.parse,urllib.error
import json
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input("Enter url :")
html=urllib.request.urlopen(url,context=ctx).read().decode()
data = json.loads(html)
count = 0
for index in data['comments']:
    num = index['count']
    count = count + num
print(count)