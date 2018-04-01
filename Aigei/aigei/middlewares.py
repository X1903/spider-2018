# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

import json
import logging
from scrapy import signals
import requests
from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.exceptions import IgnoreRequest
from scrapy.utils.response import response_status_message

from aigei.proxy import RedisClient


class ProxyMiddleware():
    def __init__(self, proxy_url):
        self.logger = logging.getLogger(__name__)
        self.proxy_url = proxy_url
        self.redis = RedisClient()
    
    def get_random_proxy(self):
        proxy = self.redis.random()
        print('Get Proxy', proxy)
        return proxy
    
    def process_request(self, request, spider):
        print('Retry Time', request.meta.get('retry_times'))
        if request.meta.get('retry_times'):
            proxy = self.get_random_proxy()
            if proxy:
                uri = 'https://{proxy}'.format(proxy=proxy)
                self.logger.debug('Using ' + proxy)
                request.meta['proxy'] = uri
    
    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(
            proxy_url=settings.get('PROXY_URL')
        )


class ErrorMiddleware(RetryMiddleware):
    def process_response(self, request, response, spider):
        reason = response_status_message(response.status)
        if request.url.startswith('http://www.aigei.com/f/d'):
            print('Response Text', response.text)
            try:
                result = json.loads(response.text)
                print('Failed, Retrying...')
                if result.get('status') == 'notEnoughCoin':
                    print('Not Enough Coin, Ignore')
                    raise IgnoreRequest
                if result.get('status') != 'success':
                    return self._retry(request, reason, spider) or response
            except json.decoder.JSONDecodeError:
                print('Json Decode Error', response.text)
                return self._retry(request, reason, spider) or response
        return response


class CookiesMiddleware():
    cookies_str = 'gei_d_u=a7f8d527fc534e00b1c6b911770308e4; oOO0OO0oOO00oo0o=true; geiweb-v=zZ+S93HA1Qc5+FCWF5rzLLAflXAQkHiNvbO6RtVUvQdZqZQ6W7Dr3C6E7yUsUIDx; wueiornjk234kj=1a4e77fc8bd04260aad53634a0c2fce6; JSESSIONID=74B802603767124060EFF91F25F8CF89; OooOO000oOOO00o=1837326'
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.cookies = self.string2dict(self.cookies_str)
    
    def string2dict(self, str):
        d = {}
        items = str.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            d[key] = value
        return d
    
    def process_request(self, request, spider):
        self.logger.debug('Setting Cookies ' + json.dumps(self.cookies))
        request.cookies = self.cookies
