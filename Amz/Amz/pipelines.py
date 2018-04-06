# -*- coding: utf-8 -*-

from pymongo import MongoClient
import redis
import hashlib

class AmzPipeline(object):

    def open_spider(self, spider):
        # 链接MongoDB
        self.client = MongoClient(host='127.0.0.1', port=27017)
        self.collection = self.client["amzon"][spider.name]

        # 链接Redis
        # self.r = redis.Redis(host='127.0.0.1', port=6379, db=2)
        # self.item_key = "item_dumpkey"

    def process_item(self, item, spider):
        print("*" * 100)
        self.collection.insert(dict(item))
        return item




    def close_spider(self, spider):
        self.client.close()

