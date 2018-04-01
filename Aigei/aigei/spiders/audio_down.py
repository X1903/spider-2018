# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from pyquery import PyQuery as pq
from selenium import webdriver
import base64
import requests
import json
from os.path import join, exists
from aigei.items import AigeiItem
from os import makedirs
import re
from scrapy import Request, FormRequest
from urllib.parse import urlencode
import time
import random


class AudioSpider(scrapy.Spider):
    name = 'audio_down'
    allowed_domains = ['www.aigei.com']
    start_url = 'http://www.aigei.com/sound/class/?order=down'
    base_url = 'http://www.aigei.com/sound/class'
    home_url = 'http://www.aigei.com/sound/class/common_classes/'
    script_file = 'main.js'
    proxy_url = 'http://localhost:5555/random'
    token_url = 'http://www.aigei.com/f/d/'
    
    def __init__(self, name=None, **kwargs):
        super(AudioSpider, self).__init__(name=name, **kwargs)
        self.driver = webdriver.PhantomJS()
        self.driver.get(self.home_url)
        self.script = open(self.script_file).read()
    
    def __del__(self):
        self.driver.quit()
    
    def start_requests(self):
        yield Request(url=self.start_url, callback=self.parse_list)
    
    def parse_list(self, response):
        doc = pq(response.text)
        results = doc('.item-info-list-body .audio-item-box-row').items()
        page = doc('.item-info-page-nav:nth-child(1) strong').text()
        for result in results:
            element = result.find('li > input:nth-child(2)')
            item = AigeiItem({
                'element': str(element).strip(),
                'title': result.find('.title-name').text(),
                'id': result.find('li').attr('itemid'),
                'category': re.sub('\s', '', doc('.page-title-big').text()),
                'duration': result.find('.duration-desc').text().strip(),
                'download': result.find('.down-num').text().strip(),
                'tags': [i.text().strip() for i in result.find('.group-dir a').items()],
                'page': page
            })
            token = self.get_token(item)
            yield FormRequest(url=self.token_url, formdata=token, callback=self.parse_audio, meta={'item': item})
        
        next_page = self.base_url + '?' + urlencode({'page': int(page) + 1, 'order': 'down', })
        yield Request(url=next_page, callback=self.parse_list)
    
    def get_token(self, item):
        js = self.script
        js += "return crawl($('{element}'))".format(element=item['element'])
        data = self.driver.execute_script(js)
        return data
    
    def parse_audio(self, response):
        print('Response text', response.text)
        item = response.meta['item']
        result = json.loads(response.text)
        audio = base64.b64decode(result.get('message')).decode('utf-8')
        print(audio)
        item['audio'] = audio
        print(item)
        yield item
