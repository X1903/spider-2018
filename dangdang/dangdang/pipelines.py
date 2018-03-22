# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql.cursors
from scrapy.conf import settings


class DangdangPipeline(object):
    def process_item(self, item, spider):
        host = settings['MYSQL_HOSTS']
        user = settings['MYSQL_USER']
        psd = settings['MYSQL_PASSWORD']
        db = settings['MYSQL_DB']
        c = settings['CHARSET']

        con = pymysql.connect(host=host, user=user, passwd=psd, db=db, charset=c)
        cur = con.cursor()


        sql = "insert into dd_books(title, link, comment) value(%s, %s, %s)"
        list = [item['title'], item['link'], item['comment']]
        cur.execute(sql, list)
        con.commit()
        cur.close()


        print('保存成功.....')

        return item


'''

建表语句

# CREATE TABLE `dd_books` (
#   `title` char(200) NOT NULL,
#   `link` char(125) DEFAULT NULL,
#   `comment` char(120) DEFAULT NULL,
#   PRIMARY KEY (`title`),
#   UNIQUE KEY `link` (`link`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8

'''