# -*- coding: utf-8 -*-
import scrapy
from ts.items import TsItem
from pyquery import PyQuery as pq
from scrapy.http import Request


class LessonSpider(scrapy.Spider):
    name = 'lesson'
    allowed_domains = ['hellobi.com']
    start_urls = ['https://edu.hellobi.com/course/1']

    def parse(self, response):
        doc = pq(response.text)
        item = TsItem()
        item['title'] = doc('.course-info h1').text()
        item['image'] = doc('.img-responsive').attr('src')
        item['link'] = doc('input[name=redirect_url]').attr('value')
        item['skus'] = doc('.course-view').text()

        yield item

        for i in range(2, 267):
            url = 'https://edu.hellobi.com/course/' + str(i)
            yield Request(url, callback=self.parse)

