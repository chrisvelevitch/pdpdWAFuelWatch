#!/usr/local/bin/python3

from urllib import request
from xml.etree import ElementTree as ET
# import lxml
import sys
# import urllib3

print('---start---')
print('version: '+sys.version)
print(dir(sys))
print(sys.path)
print(sys.path_importer_cache)
response = request.urlopen('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=4')
print(str(response))
print('---step 1---')
headers = response.info()
print(str(headers))
print('---step 2---')
print(type(response))
r = response.read()
data = r.decode('utf-8')
print(type(data))
print('---step 3---')
x = ET.fromstring(data)
print(type(x))
print(x.tag)
print(x.findall(".//item"))
print('---step 4---')
items = x.findall(".//item")
print(len(items[0]))
prices = []
for i1 in items:
    d = {}
    for i in i1:
        d[i.tag] = str(i.text)
    # print(str(d))
    prices.append(d)
print('---step 5---')

def by(i):
    return 'price'

print(str(sorted(prices, key=by)))
print('---end---')
