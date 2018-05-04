# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HebeiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tt_url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    img = scrapy.Field()

    classUrl = scrapy.Field()
    cls = scrapy.Field()






    pass
