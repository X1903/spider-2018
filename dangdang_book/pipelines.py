# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib
import redis
from pymongo import MongoClient

class BookPipeline(object):
    def open_spider(self,spider):
        self.r = redis.Redis(host,port)
        self.item_key = "item_dumpkey"
        client = MongoClient(host,port)
        self.collection = client["book"][spider.name]


    def process_item(self, item, spider):
        item_exist = self.item_dupfilter(item)
        if not item_exist:
            self.collection.insert(item)
        return item

    def item_dupfilter(self,item):
        f = hashlib.sha1()
        f.update(item["book_name"].encode())
        f.update(item["author"].encode())
        fingerprint = f.hexdiget()
        added = self.r.sadd(self.item_key,fingerprint)
        return added==0
