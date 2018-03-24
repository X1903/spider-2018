# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from scrapy.conf import settings

class JdPipeline(object):
    def process_item(self, item, spider):
        print('+-' * 50)
        print(item)
        host = settings['MYSQL_HOSTS']
        user = settings['MYSQL_USER']
        psd = settings['MYSQL_PASSWORD']
        db = settings['MYSQL_DB']
        c = settings['CHARSET']

        con = pymysql.connect(host=host, user=user, passwd=psd, db=db, charset=c)
        cur = con.cursor()

        sql = "insert into jd_goods(title, shop, shoplink, price, comment) value(%s, %s, %s, %s, %s)"
        list = [item['title'], item['shop'], item['shoplink'], item['price'], item['comment']]
        cur.execute(sql, list)
        con.commit()
        cur.close()

        print('保存成功.....')
        print('+-'*50)

        return item



'''
title = scrapy.Field()
shop = scrapy.Field()
shoplink = scrapy.Field()
price = scrapy.Field()
comment = scrapy.Field()



# CREATE TABLE `dd_books` (
#   `title` char(200) NOT NULL,
#   `link` char(125) DEFAULT NULL,
#   `comment` char(120) DEFAULT NULL,
#   PRIMARY KEY (`title`),
#   UNIQUE KEY `link` (`link`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8


create table jd_goods(
    title char(200) not null,
    shop char(50),
    shoplink char(125),
    price char(10),
    comment char(10)
    
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
