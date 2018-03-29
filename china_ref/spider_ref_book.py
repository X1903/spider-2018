# coding=utf-8
"""
爬取中国裁判文书网部分数据
网址: http://wenshu.court.gov.cn/
分析: 
1.从http://wenshu.court.gov.cn/ValiCode/GetCode发起post请求拿到真正请求的number参数
2.向http://wenshu.court.gov.cn/List/ListContent发起请求,获取数据
** 注意1和2中post的请求体的guid的值要一致
** cookie中的vjk15和post请求体中的v15x要匹配

"""
import requests
import time
import json


class RefBookSpider(object):

    def __init__(self):
        self.file = open('ref_book.json', 'w+', encoding='utf-8')
        # 构造url
        self.url = 'http://wenshu.court.gov.cn/List/ListContent'
        self.get_code_url = 'http://wenshu.court.gov.cn/ValiCode/GetCode'
        # 构造请求头
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like "
                          "Gecko) Chrome/62.0.3202.94 Safari/537.36",
            "Cookie": "vjkl5=017e48b5a0ffd8deaf01a51865ba9365cdfc868f"
        }
        # 构造请求数据
        self.data = {
            'Param': '案件类型:刑事案件',
            # 'Index': '1', 页数需要相加
            # 'number': JDH43K, number临时获取
            'Page': '20',
            'Order': '法院层级',
            'Direction': 'asc',
            'vl5x': '62159c9dc3c71bcde6e4411a',
            'guid': 'af951fc1-4f95-50765106-99a21d4d9bc8',
        }
        self.get_code_data = {
            'guid': 'af951fc1-4f95-50765106-99a21d4d9bc8',
        }
        # 断点续传
        try:
            f = open('download_index.txt', 'r')
            index = int(f.read())
            self.index = index
        except:
            self.index = 1

    def get_data(self):
        # 发起请求,接受number
        res = requests.post(self.get_code_url, headers=self.headers,
                            data=self.get_code_data)
        number = res.content.decode()
        # 完善请求体
        self.data['number'] = number
        self.data['Index'] = self.index
        print('正在下载第%s页数据---------' % self.index)
        # 发起请求,接受真正的数据
        response = requests.post(self.url, headers=self.headers,
                                 data=self.data)
        # 返回数据
        self.index += 1
        return response.content.decode()

    def parse_data(self, data):
        # 解析响应
        # 去除满山遍野的反斜杠
        data_str = data.replace('\\', "").strip('"')
        data_list = json.loads(data_str)
        # 有时会下载数据失败,重新下载
        if not data_list:
            self.index -= 1
            print('下载第%s页失败=======' % self.index)
            return
        for ref_book in data_list[1:]:
            print('正在保存:', ref_book)
            save_str = json.dumps(ref_book, ensure_ascii=False) + ',\n'
            self.file.write(save_str)

    def run(self):
        while True:
            data = self.get_data()
            self.parse_data(data)
            time.sleep(2)

    def __del__(self):
        self.file.close()
        with open('download_index.txt', 'w') as f:
            f.write(str(self.index))

if __name__ == '__main__':
    spider = RefBookSpider()
    spider.run()
