# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

import os
from flask import Flask, request, render_template, jsonify, send_from_directory
from bson import json_util
import json
from pymongo import MongoClient
import redis
from datetime import datetime

# MongoDB数据信息配置
# MONGO_HOST = '47.106.66.56'
MONGO_HOST = '47.106.66.56'
MONGO_PORT = 27017


# Redis数据信息配置
# REDIS_HOST = '47.106.66.56'
REDIS_HOST = '47.106.66.56'
REDIS_PORT = 6379
REDIS_PASSWORD = 'Panda112233'

# 评论的URL
comment_url = 'https://www.amazon.{}/product-reviews/{}?pageSize=10&pageNumber=1'
# redis数据
task_key = 'Amazon_spider:start_urls'




# 爬虫
import csv
import urllib.request
from pyquery import PyQuery as pq
from datetime import datetime
import time
import ssl
context = ssl._create_unverified_context()
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"}



# def save_csv(list, fileName):
#     '''保存文件到csv'''
#     with open(fileName, 'a+', errors='replace', encoding='utf8') as f:
#         save = csv.writer(f, dialect='excel')
#         save.writerow(list)





class RedisClient(object):
    '''初始化Redis数据库'''
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)

    def lpush(self, key, coent):
        try:
            self.db.lpush(key, coent)
        except Exception as e:
            print(e)


class MongodbClient(object):
    '''初始化MongoDB数据库'''

    def __init__(self):
        self.client = MongoClient(MONGO_HOST, MONGO_PORT)
        self.db = self.client['Amazon']


    def get_one_form_oid(self, asin):
        '''查询指定ID的数据'''
        # return self.db.Amazon.find_one({'Asin':asin}).skip(10).limit(10)
        return self.db.Amazon.find_one({'Asin':asin})


    def add_one(self, url, Asin, Country):
        '''新增数据'''

        data = str((datetime.now()))
        post = {
            'Url':url,
            'Asin':Asin,
            'Country':Country,
            'CreatedDate':data[0:19] # 截取日期和时间
        }

        # 插入一条新数据
        self.db.Amazon.insert_one(post)

    def update(self, asin):
        '''修改数据'''

        # 修改一条数据
        data = str(datetime.now())
        self.db.Amazon.update({'Asin':asin}, {'$set':{'updateData':data[0:19]}})
        self.db.Amazon.update({'Asin':asin}, {'$unset':{'CommentAll':''}}, False, True)




app = Flask(__name__)


def toJson(data):
    '''转换成json数据'''
    return json.dumps(
        data,
        default=json_util.default,
        ensure_ascii=False
    )



@app.route('/adds', methods=["POST"])
def add_works():
    '''添加任务'''

    # try:
    data_json = request.get_json()

    datas = data_json['Infos']
    for data in datas:

        print(data)
        print("*"*100)


        # 判断是那个国家的URL
        Country = data['Country']
        if Country == 'US':
            domain = 'com'
        elif Country == 'GB':
            domain = 'co.uk'
        else:
            domain = 'ca'


        asins = data['ASINs'].split(',')

        # 变量获取
        for asin in asins:

            # 拼接完整的URL
            url = comment_url.format(domain, asin)


            #URL添加到redis
            # print(task_key, url)
            redis_conn = RedisClient()
            redis_conn.lpush(task_key, url)


            #创建或更新MongoDB商品评论表

            mongo_conn = MongodbClient()
            # 判断是否添加过
            if mongo_conn.get_one_form_oid(asin):
                # asin已添加就更新
                mongo_conn.update(asin)
            else:
                # 第一次创建任务
                mongo_conn.add_one(url, asin, Country)
    return "添加成功"
    # except Exception as e:
    #     print(e)
    #
    # return '添加失败'


@app.errorhandler(404)
def page_not_found(e):
    '''处理404页面'''
    return render_template('404.html')


@app.route('/', methods=['GET'])
def index():
    '''搜索首页'''
    if request.method == 'GET':
        # 链接数据库
        mongo_conn = MongodbClient()
        # 获取评论商品总数
        total = mongo_conn.db.Amazon.count()
        return render_template('index.html', total=total)



# 搜索展示页面
@app.route('/search', methods=['GET'])
@app.route('/search/<item>', methods=['GET'])
def get_goods(item=None):
    '''返回查询数据'''
    if request.method == 'GET':
        terrace = request.values.get('terrace')        # 平台
        asin = request.args.get('Asin')                # 商品ID
        sta_date = request.args.get('start_date')      # 开始日期
        end_date = request.args.get('end_date')        # 结束日期
        country = request.args.get('country')          # 国家编号
        page = request.args.get('page', 1, type=int)   # 页码

        print(sta_date)
        print(end_date)


        # 判断参数是否完整
        if all([terrace, asin, country, page]):

            # 根据关键字判断数据库
            if terrace == 'Amazon':
                # 链接数据库
                mongo_conn = MongodbClient()
                datas = mongo_conn.db.Amazon.find_one({'Asin':asin})


                try:
                    commentData = datas['CommentAll']
                except Exception as e:
                    return "没有查询到数据"

                # 按照日期查询, 查询到的数据添加到列表
                commentAll_list = []
                for i in range(len(commentData)):
                    print(commentData[i])

                    if commentData[i]['CommentTime'] > sta_date  and commentData[i]['CommentTime'] < end_date:
                        print(commentData[i]['CommentTime'])
                        commentAll_list.append(commentData[i])


                # 根据日期排序
                def get_end_last(data):
                    return data.sort(key=lambda s: s['CommentTime'])
                get_end_last(commentAll_list)


                # 按页码返回数据
                sta_page = (page-1)*10
                end_page = sta_page + 50
                data = commentAll_list[sta_page:end_page]

                return toJson(data)
        else:
            return '参数不完整'



def save_csv(list, fileName):
    '''保存文件到csv'''
    with open(fileName, 'w+', errors='replace', encoding='utf8') as f:
        for item in list:
            save = csv.writer(f, dialect='excel')
            save.writerow(item)


# @app.route('/parities/as', methods=['GET'])
@app.route('/parities/<path:filename>', methods=['GET'])
def parities(filename):
    '''各类货币兑美元电汇牌价下载'''
    if request.method == 'GET':

        # 下载目录，从工程的根目录写起
        dirpath = os.path.join(app.root_path, 'files')

        fileList = os.listdir(dirpath)
        if filename not in fileList:
            print("*"*100)

            fileName = "./files/货币兑美元电汇牌价" + str(datetime.now())[0:10] + '.csv'
            url = "https://www.bochk.com/whk/rates/exchangeRatesUSD/exchangeRatesUSD-input.action?lang=cn"
            resp = urllib.request.Request(url, headers=headers)
            pagedata = urllib.request.urlopen(resp, context=context).read().decode("utf-8", "ignore")
            doc = pq(pagedata)
            tr = doc(".import-data tr:even")

            dataList = []
            for item in tr:
                title = item[0].text.split()

                buy = item[1].text.split()
                sale = item[2].text.split()
                data = title + buy + sale
                dataList.append(data)
            save_csv(dataList, fileName)
            time.sleep(1)

            if filename not in fileList:
                dataNum = filename[9:19]

                return dataNum + "的信息没有收录或者文件名输入错误"

        # as_attachment=True 一定要写，不然会变成打开，而不是下载
        return send_from_directory(dirpath, filename, as_attachment=False)




if __name__ == '__main__':
    # app.run(host='0.0.0.0',threaded=True)
    app.run(debug=True,threaded=True)
