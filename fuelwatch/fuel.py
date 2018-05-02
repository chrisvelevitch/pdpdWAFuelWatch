#!/usr/local/bin/python3

from urllib import request
from xml.etree import ElementTree as ET
import sys

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
fuelRecords = x.findall(".//item")
print('Found '+str(len(fuelRecords))+' fuel records')
prices = [
    {
        xmlFuelRecord.tag: str(xmlFuelRecord.text)
        for xmlFuelRecord in fuelRecord
    }
    for fuelRecord in fuelRecords
]

def by(i):
    return 'price'
prices = sorted(prices, key=by)
print('---step 5---')
for price in prices:
    print('name:' + price['trading-name'])
print(prices[0].keys())
print('---end---')
