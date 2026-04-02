import json
data = '''
{"name":"sam",
"phone":{"type" : "intl","number" : "+91 7 788 996 655"},
"email":{ "hide"  : "yes"}}'''
jdata = json.loads(data)
print("NAME : ",jdata['name'])
print("PHONE NUMBER : ",jdata['phone']['number'])
print("EMAIL : ",jdata['email']['hide'])