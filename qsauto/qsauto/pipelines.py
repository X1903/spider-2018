# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class QsautoPipeline(object):
    def process_item(self, item, spider):

        print('+-'*50)


        with open('qiushibaike.text', 'a') as f:
            # f.write(json.loads(item))
            f.write(str(item['content']) + '\n')
            print('保存成功')
        return item
