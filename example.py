import time
import os
import json
import requests
from bs4 import BeautifulSoup
import csv
import sys
from time import sleep
from time import gmtime, strftime
import matplotlib.pyplot as plt

enddate = strftime("%Y%m%d", gmtime())
r  = requests.get("https://coinmarketcap.com/currencies/contentos/historical-data/?start=20140101&end={0}".format(enddate))
data = r.text

soup = BeautifulSoup(data, "html.parser")
table = soup.find('table', attrs={ "class" : "table"})

prices = []

for row in table.find_all('tr'):
    addPrice = False
    tag = row.findAll('td')
    for val in tag:
        value = val.text

        if "Sep 10" in value:
            print(value)
            addPrice = True

    if addPrice == True:
        prices.append( tag[3].text )

# flip list, months are in reverse order
prices = prices[::-1]
for i in range(0,len(prices)):
    prices[i] = float(prices[i])

#for price in prices:
#    price = float(price)
print(prices)
x = list(range(0, len(prices)))
print(x)

x = list(range(0, len(prices)))

plt.title('contentos price from 2014')
plt.ylabel('Price in USD')
plt.xlabel('Years from 2014')
plt.bar(x, prices)

os.system("rm -rf chart.png")
time.sleep(1)
plt.savefig('chart.png')
