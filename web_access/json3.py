import urllib.request,urllib.parse,urllib.error
import json, ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'
address = input("Enter address :")
address = address.strip()
parm = dict()
parm['q'] = address
url = serviceurl + urllib.parse.urlencode(parm)
html = urllib.request.urlopen(url,context=ctx).read().decode()
loc = json.loads(html)
for i in loc:
    print(loc['features'][0]['properties']['plus_code'])