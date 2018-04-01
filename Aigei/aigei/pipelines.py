# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import requests
from os.path import exists, join
from os import makedirs


class AigeiPipeline(object):
    folder = './audios'
    
    def process_item(self, item, spider):
        item = dict(item)
        with requests.get(item['audio']) as response:
            folder = join(self.folder, item['category'], item['page'])
            if not exists(folder):
                makedirs(folder)
            with open(join(folder, item['title'] + '.mp3'), 'wb') as f:
                f.write(response.content)
            with open(join(folder, item['title'] + '.json'), 'w', encoding='utf-8') as f:
                f.write(json.dumps(item, ensure_ascii=False))
        return item
