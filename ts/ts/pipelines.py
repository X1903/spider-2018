# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TsPipeline(object):
    def __init__(self):
        self.fh = open('./hellobi.txt', 'a')

    def process_item(self, item, spider):

        print(item['title'])
        print(item['link'])
        print(item['skus'])
        print(item['image'])

        self.fh.write(str(item['title'] + '\n'))
        self.fh.write(str(item['link'] + '\n'))
        self.fh.write(str(item['skus'] + '\n'))
        self.fh.write(str(item['image'] + '\n'))
        self.fh.write('\n\n\n')
        print('保存成功+++++++++++++++++++++++')


        return item

    def close_spider(self):
        self.fh.close()
