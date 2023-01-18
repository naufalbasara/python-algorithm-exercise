import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Naufal</name>
    <phone type="intl">
        +62 8155123456
    </phone>
    <email hide="yes"/>
</person>
'''

tree = ET.fromstring(data)
print('Name: ', tree.find('name').text)
print('Phone: ', tree.find('phone').text)
print('Phone: ', tree.find('email').get('hide'))


input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="3">
            <id>009</id>
            <name>Naufal</name>
        </user>
    </users>
</stuff>
'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User Count: ', len(lst))
for item in lst:
    print('Name: ', item.find('name').text)
    print('Id: ', item.find('id').text)
    print('Attributes: ', item.get('x'))