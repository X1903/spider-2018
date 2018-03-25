# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qsauto.items import QsautoItem
from pyquery import PyQuery as pq
from scrapy.http import Request

root_url = 'https://www.qiushibaike.com/'

class Qsbk1Spider(CrawlSpider):
    name = 'qsbk1'
    allowed_domains = ['qiushibaike.com']
    # start_urls = ['http://qiushibaike.com/']

    # 防止第一URL301
    def start_requests(self):
        ua = {"User-Agent":'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'}
        yield Request('http://www.qiushibaike.com/', headers=ua)

    rules = (
        Rule(LinkExtractor(allow=r'article'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        doc = pq(response.text)
        item = QsautoItem()
        item['content'] = doc('.content').text()
        item['link'] = root_url + str(doc('link[rel=canonical]').attr('href'))

        return item
