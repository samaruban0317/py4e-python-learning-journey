import xml.etree.ElementTree as ET
data = '''<person>
<name>SAMARUBAN</name>
<age type = 'intl'>17</age>
<email hide='yes'/>
</person>'''
tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Email:',tree.find('email').get('hide'))
x=tree.find('age').text

print(x,type(x))
