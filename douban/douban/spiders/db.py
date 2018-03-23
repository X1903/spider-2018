# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest
from pyquery import PyQuery as pq
import urllib.request

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


class DbSpider(scrapy.Spider):
    name = 'db'
    allowed_domains = ['douban.com']
    # start_urls = ['http://douban.com/']

    context = ssl._create_unverified_context()
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'}

    def start_requests(self):
        return [Request('https://accounts.douban.com/login', headers=self.header, callback=self.parse, meta={'cookiejar': 1})]

    def parse(self, response):
        doc = pq(response.text)

        # 图片路径
        captcha = doc('#captcha_image').attr('src')
        print(captcha)
        if len(captcha) > 0:
            print('有验证码....处理验证码....')

            # 保存验证码到本地
            localpath = './captcha.png'
            urllib.request.urlretrieve(captcha, localpath)

            # 输入验证码
            print("请查看本地验证码..并输入验证码内容")
            captcha_code = input('输入验证码: ')

            data = {
                'form_email': '15999999999',
                'form_password': '88888888',
                'captcha-solution':captcha_code,
                'redir': 'https://www.douban.com/people/170943828/',
            }
            return [FormRequest.from_response(
                response,
                meta={'cookiejar': response.meta['cookiejar']},
                headers=self.header,
                formdata=data,
                callback=self.next,
            )]


        else:

            data = {
                'form_email': '15999692363',
                'form_password': 'xy930808',
                'redir': 'https://www.douban.com/people/170943828/'
            }
            print('无验证码登录中...')
            print('*'*200)
            return [FormRequest.from_response(
                response,
                meta={'cookiejar': response.meta['cookiejar']},
                headers = self.header,
                formdata=data,
                callback=self.next,
            )]


    # 登陆后的回调函数
    def next(self, response):
        print('登录完成')
        doc = pq(response.text)
        title = doc('title').text()
        note = doc('.note p').text()



        print(title)
        print(note)
