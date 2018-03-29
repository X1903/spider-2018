# coding=utf-8
# 尝试下载数据
import requests


class RefBookSpider(object):

    def __init__(self):
        # 构造url
        self.url = 'http://wenshu.court.gov.cn/List/ListContent'
        # 构造请求头
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like "
                          "Gecko) Chrome/62.0.3202.94 Safari/537.36",
            "Cookie": "vjkl5=017e48b5a0ffd8deaf01a51865ba9365cdfc868f"
        }
        # 构造请求数据
        self.data = {
            'Param': '案件类型:刑事案件',
            'Index': '1',
            'Page': '20',
            'Order': '法院层级',
            'Direction': 'asc',
            'vl5x': '62159c9dc3c71bcde6e4411a',
            'guid': 'af951fc1-4f95-50765106-99a21d4d9bc8',
        }
        self.get_code_data = {
            'guid': 'af951fc1-4f95-50765106-99a21d4d9bc8',
        }
        self.get_code_url = 'http://wenshu.court.gov.cn/ValiCode/GetCode'

    def run(self):
        # 发起请求,获取code
        response = requests.post(self.get_code_url, headers=self.headers, data=self.get_code_data)
        # 验证响应
        print(response.content.decode())
        print(response.status_code)
        # 获取code
        code = response.content.decode()
        self.data['number'] = code
        # 发起请求,接受响应
        response = requests.post(self.url, headers=self.headers, data=self.data)
        with open('text2.html', 'w', encoding='utf-8') as f:
            f.write(response.content.decode())
        # 输出
        print(response.status_code)
        print(response.content.decode())

if __name__ == '__main__':
    spider = RefBookSpider()
    spider.run()

