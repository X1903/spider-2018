# coding=utf-8
import requests
from requests.utils import dict_from_cookiejar


class RefBookSpider(object):
    def __init__(self):
        self.url = 'http://wenshu.court.gov.cn/List/List?sorttype=1&conditions=searchWord+1' \
                   '+AJLX++%E6%A1%88%E4%BB%B6%E7%B1%BB%E5%9E%8B:%E5%88%91%E4%BA%8B%E6%A1%88%E4%BB%B6'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like "
                          "Gecko) Chrome/62.0.3202.94 Safari/537.36"
        }

    def run(self):
        response = requests.get(self.url, headers=self.headers)
        print(dict_from_cookiejar(response.cookies))
        with open('text1.html', 'w', encoding='utf-8') as f:
            f.write(response.content.decode())

if __name__ == '__main__':
    spider = RefBookSpider()
    spider.run()
