import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')

counts = int(input('Enter Count: '))

position = int(input('Enter Position: '))


def getLocAndName(curr_url, pos):

    html = urllib.request.urlopen(curr_url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    link_encounter = 1
    for tag in tags:
        curr_link = tag.get('href', None)
        curr_name = tag.contents[0]
        if link_encounter == pos:
            return curr_link, curr_name
        link_encounter += 1


curr_url = url
lastvalue = ""
print('Retrieving: ', curr_url)
for cnt in range(counts):
    curr_url, curr_name = getLocAndName(curr_url, position)
    # print("{} --> {} ".format(curr_url, curr_name))
    lastvalue = curr_name
    print('Retrieving: ', curr_url)

print(lastvalue)
