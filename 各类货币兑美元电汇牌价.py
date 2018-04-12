# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

import csv
import urllib.request
from pyquery import PyQuery as pq
from datetime import datetime

import ssl
context = ssl._create_unverified_context()

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"}


url="https://www.bochk.com/whk/rates/exchangeRatesUSD/exchangeRatesUSD-input.action?lang=cn"
resp = urllib.request.Request(url, headers=headers)
pagedata=urllib.request.urlopen(resp, context=context).read().decode("utf-8","ignore")

doc = pq(pagedata)



def save_csv(list, fileName):
    with open(fileName, 'a+', errors='replace', encoding='utf8') as f:
        save = csv.writer(f, dialect='excel')
        save.writerow(list)

fileName = "各类货币兑美元电汇牌价" +str(datetime.now())[0:19] + '.csv'

tr = doc(".import-data tr:even")
for item in tr:
    title = item[0].text.split()

    buy = item[1].text.split()
    sale = item[2].text.split()
    data = title+buy+sale
    save_csv(data, fileName)








# print(pagedata)
# pat='<div class="content">.*?<span>(.*?)</span>.*?</div>'
