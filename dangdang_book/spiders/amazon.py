# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import  RedisCrawlSpider

class AmazonSpider(RedisCrawlSpider):
    name = 'amazon'
    allowed_domains = ['amazon.cn']
    # start_urls = ['http://amazon.cn/']
    redis_key = "amazon"

    rules = (
        #提取大分类的url地址，请求
        #提取小分类的url地址，请求
        Rule(LinkExtractor(restrict_xpaths="//div[@class='categoryRefinementsSection']/ul/li"), callback="parse_book_list",follow=True),

    )

    def parse_book_list(self, response):
        li_list = response.xpath("//div[@id='mainResults']/ul/li")
        for li in li_list:
            item = {}
            item["book_title"] = li.xpath(".//h2/text()").extract_first()
            item["book_img"] = li.xpath(".//img[@class='s-access-image cfMarker']/@src").extract_first()
            item["book_price"]= li.xpath(".//div[@class='a-column a-span7']/div[@class='a-row a-spacing-none'][2]//span[@class='a-size-base a-color-price s-price a-text-bold']/text()").extract_first()
            item["book_author"]= li.xpath(".//div[@class='a-row a-spacing-small']/div[2]/span/text()").extract()
            item["book_comments_num"] = li.xpath(".//div[@class='a-column a-span5 a-span-last']/div/a/text()").extract_first()
            item["book_href"] = li.xpath(".//h2/../@href").extract_first()
            if item["book_href"] is not None:
                yield  scrapy.Request(
                    item["book_href"],
                    callback=self.parse_book_detail,
                    meta={"item":item}
                )

    def parse_book_detail(self,response):
        item = response.meta["item"]
        item["cate_info"] = response.xpath("//ul[@class='a-unordered-list a-horizontal a-size-small']/li[not(@class)]//text()").extract()
        item["cate_info"] = [i.strip() for i in item["cate_info"] if len(i.strip())>0]
        print(item)
