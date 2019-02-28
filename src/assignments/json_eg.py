import ssl
import urllib.request, urllib.parse, urllib.error
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)

uh = urllib.request.urlopen(url)
data = uh.read().decode()
# print(data)

print('Retrieved', len(data), 'characters')

info = json.loads(data)
lst = list()
for item in info['comments']:
    v = item['count']
    lst.append(v)
print('Count: ', len(lst))
print('Sum: ', sum(lst))
