# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jd.items import JdItem
import re
import urllib.request


import ssl
ssl._create_default_https_context = ssl._create_unverified_context



class JdGoodsSpider(CrawlSpider):
    name = 'jd_goods'
    allowed_domains = ['jd.com']
    start_urls = ['https://list.jd.com/list.html?cat=670,671,2694&ev=exbrand_17440']

    rules = (
        Rule(LinkExtractor(allow=''), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        try:
            item = JdItem()
            thisurl = response.url
            pat = "item.jd.com/(.*?).html"
            x = re.search(pat, thisurl)
            if (x):
                # 获取商品ID
                thisid = re.compile(pat).findall(thisurl)[0]

                # 获取商品title
                item['title'] = response.xpath("//div[@class='sku-name']/text()").extract()
                # 获取商品
                item['shop'] = response.xpath("//div[@class='name']/a/text()").extract()
                # 商品链接
                item['shoplink'] = response.xpath("//div[@class='name']/a/@href").extract()


                # 价格接口链接
                priceurl = "https://p.3.cn/prices/get?type=1&area=1_72_2799&pdtk=&pduid=1888909243&pdpin=&pdbp=0&skuid=J_" + str(thisid) + "&callback=cnp"

                # 获取价格
                pricedata = urllib.request.urlopen(priceurl).read().decode("utf-8", "ignore")
                pricepat = '"p":"(.*?)"'
                item['price'] = re.compile(pricepat).findall(pricedata)

                # 评论接口链接
                commenturl = "https://sclub.jd.com/comment/productPageComments.action?productId=" + str(thisid) + "&score=0&sortType=3&page=0&pageSize=10&callback=fetchJSON_comment98vv4956"

                # 获取评论
                commentdata = urllib.request.urlopen(commenturl).read().decode("utf-8", "ignore")
                commentpat = 'goodRateShow":(.*?),'
                item['comment'] = re.compile(commentpat).findall(commentdata)
                yield item

        except Exception as e:
            print(e)






'''
title = scrapy.Field()
shop = scrapy.Field()
shoplink = scrapy.Field()
price = scrapy.Field()
comment = scrapy.Field()
'''