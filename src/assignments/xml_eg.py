import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter location: ')

print('Retrieving', url)

uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
lst1 = list()

for item in lst:
    # print(item.find('name').text)
    counts = int(item.find('count').text)
    lst1.append(counts)
print('Count: ', len(lst1))
print('Sum: ', sum(lst1))
