# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 标题
    title = scrapy.Field()

    # 链接
    link = scrapy.Field()

    # 评论数
    comment = scrapy.Field()
