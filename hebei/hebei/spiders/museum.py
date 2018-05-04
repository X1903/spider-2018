# -*- coding: utf-8 -*-


import scrapy
from pyquery import PyQuery as pq

from hebei.items import HebeiItem
import copy


class MuseumSpider(scrapy.Spider):
    name = 'museum'
    allowed_domains = ['www.hebeimuseum.org']
    start_urls = ['http://www.hebeimuseum.org/channels/175.html']
    base_url = "http://www.hebeimuseum.org"



    def parse(self, response):
        doc = pq(response.text)
        class_list = doc('.inner .bd ul li').items()
        item = HebeiItem()
        for cls in class_list:
            item['cls'] = cls.text()                                    # 类名
            item['classUrl'] =  self.base_url + cls('a').attr('href')   # 类URL
            yield scrapy.Request(
                item['classUrl'],
                callback=self.class_detail,
                meta={'item':copy.deepcopy(item)})

    def class_detail(self, response):
        item = response.meta["item"]
        doc = pq(response.text)
        item_list = doc('.pgwSlideshow li').items()
        for i in item_list:
            item['title'] = i('img').attr('alt')                        # 标题
            item['img'] = self.base_url + i('img').attr('src')          # imgURL
            print(item)







    # def parse(self, response):
    #     li_list = response.xpath("//div[@class='bd']/ul/li")
    #     for li in li_list:
    #         item = HebeiItem()
    #         usrl = li.xpath("./a/@href").extract_first()
    #
    #         if 'http://www.hebeimuseum.org' in usrl:
    #             tt_url = usrl
    #         else:
    #             tt_url = self.base_url + usrl
    #
    #         print(tt_url)
    #         item['tt_url'] = tt_url
    #         yield scrapy.Request(
    #             tt_url,
    #             callback=self.parse_deal,
    #             meta={'item': item}
    #         )
    #
    # def parse_deal(self, response):
    #     # href_list = response.xpath("//div[@class='ps-current']")
    #
    #     img_url = response.xpath("//ul[@class='pgwSlideshow']/li/img/@src").extract()
    #
    #     for url in img_url:
    #         if 'http://www.hebeimuseum.org' in url:
    #             img = url
    #         else:
    #             img = self.base_url + url
    #
    #             item = response.meta['item']
    #             # item['content'] = response.xpath("//ul[@class='pgwSlideshow']/li/img/@data-description").extract()
    #             item['title'] = response.xpath("//ul[@class='pgwSlideshow']/li/img/@alt").extract_first()
    #             item['img'] = img
    #
    #             yield item





