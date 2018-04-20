# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

import csv
from pyquery import PyQuery as pq
from datetime import datetime
import requests

import ssl
context = ssl._create_unverified_context()

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"}



def save_csv(list, fileName):
    '''保存文件到csv'''
    with open(fileName, 'w+', errors='replace', encoding='utf8') as f:
        for item in list:
            save = csv.writer(f, dialect='excel')
            save.writerow(item)

fileName = "招商香港电汇牌价" +str(datetime.now())[0:11] + '.csv'


def spider():
    '''爬虫抓取任务'''
    url="http://hk.cmbchina.com/rate/CmbQuote.aspx"
    data = requests.get(url, headers=headers)

    # 定义一个大的列表, 保存表格每一行的数据
    cmbchinaList = []

    # 提取title信息
    doc = pq(data.text)
    titleTdList = doc('table tr:eq(0) td').remove('br').items()


    titleList = []
    for td in titleTdList:
        title = str(td.text().replace(' ', ''))
        titleList.append(title)
    cmbchinaList.append(titleList)

    # 提取表格的内容信息, gt(0)表示从第二行开始
    contentTrList = doc('table tr:gt(0)').items()
    for item in contentTrList:
        tdLists = item('td').items()
        tdList = []
        for td in tdLists:
            tdList.append(td.text())
        cmbchinaList.append(tdList)

    save_csv(cmbchinaList, fileName)
