# -*- coding: utf-8 -*-
import scrapy
import copy
from scrapy.http import Request
from dangdang.items import DangdangItem
from pyquery import PyQuery as pq


class DdSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.54.06.00.00.00.html']

    def parse(self, response):
        doc = pq(response.text)
        item = DangdangItem()

        list = doc('ul.bigimg li').items()

        for li in list:
            item['title'] = li('p.name a').text()
            item['link'] = li('p[name=title] a').attr('href')
            item['comment'] = li('.search_comment_num').text()

            yield item

        # 获取下一页的URL
        next_url = doc('a[title=下一页]').attr('href')
        if next_url:
            next_url= 'http://category.dangdang.com/' + next_url
            yield Request(next_url,callback=self.parse)

        # yield item




