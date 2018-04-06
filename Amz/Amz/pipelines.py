# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql
import json

# MYSQL_HOST = '47.106.66.56'
# MYSQL_DBNAME = 'amoze'
# MYSQL_USER = 'root'
# MYSQL_PASSWD = 'Panda112233'

# MYSQL_HOST = '127.0.0.1'
# MYSQL_DBNAME = 'amoze'
# MYSQL_USER = 'root'
# MYSQL_PASSWD = 'q8022761'
#
#
# class AmzPipeline(object):
#
#     def __init__(self):
#         # 连接数据库
#         self.connect = pymysql.connect(
#             host=MYSQL_HOST,
#             db=MYSQL_DBNAME,
#             user=MYSQL_USER,
#             passwd=MYSQL_PASSWD,
#             charset='utf8',
#             use_unicode=True)
#
#         # 通过cursor执行增删查改
#         self.cursor = self.connect.cursor()
#
#     def process_item(self, item, spider):
#         print("*_"*100)
#         try:
#             d_json = json.dumps(item['suoyou'])
#             sql = pymysql.escape_string(d_json)
#             # 插入数据
#             self.cursor.execute("insert into amzon_con(coent) VALUES ('{}')".format(sql))
#             # 提交sql语句
#             self.connect.commit()
#             print("保存成功","*"*100)
#
#         except Exception as error:
#             # 出现错误时打印错误日志
#             print(sql)
#             print(error, '2222')
#         return item




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

