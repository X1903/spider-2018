# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

import re

import requests
import json
import pymongo

# http://www.youyee.org/youyee/viewpoint/index.html

class MongoClient(object):

    def __init__(self):
        self.client = pymongo.MongoClient(host='127.0.0.1', port=27017)
        self.db = self.client['Youyee']

    def addToDB(self, item):
        self.db.youyee.insert(dict(item))

db = MongoClient()

for i in range(0,1000, 2):
    thisurl = "http://www.youyee.org/youyee/viewpoint/amfphp/json.php?YouYeeWriting.getRecentPostList/"+str(i)+"/2/true"
    datas = requests.get(url=thisurl).text

    # print(type(datas.split('},')))

    # d_list = datas.split('},')
    # for i in d_list:
    #     print(i)

    for item in json.loads(datas):
        db.addToDB(item)
        print(item)
        print('保存成功.....')






'''

print(item)
print(item['id'])
print(item['publishtime'])
print(item['title'])
print(item['author'])
print(item['email'])
print(item['content'])
print(item['view_time'])
print(item['reply_time'])
print(item['reply_time'])
print(item['image_path'])
print(item['lastpost'])
print(item['url'])
print(item['categories'])
print(item['pubDate'])
print(item['category'])

print(item['category'])

        '''




''''

{'id': '126', 'publishtime': '2015-05-16 04:45:58', 'title': '不忘初心', 'author': 'YouYee', 'email': 'youyee@youyee.org', 'content': '<p align="left"><font face="Verdana" color="#000000">    好久没有更新微博了，哪怕连生活的点滴都常常忘记跑到这纪录。有了智能手机，有了\x08朋友圈，似乎已经忘记有博客这件事情了。偶尔回到这里，看看，想想。找找迷失的自己，发现，一切都还是那么可爱，一切都还是仿佛发生在昨天。</font></p>', 
'view_time': '556', 'reply_time': '2', 'image_path': '', 'lastpost': '2015-06-08 02:38:27', 'url': '', 'categories': '16', 'pubDate': '1431773158', 'category': 'Life'}


[{"id":"126","publishtime":"2015-05-16 04:45:58","title":"\u4e0d\u5fd8\u521d\u5fc3","author":"YouYee","email":"youyee@youyee.org","content":"<p align=\"left\"><font face=\"Verdana\" color=\"#000000\">    \u597d\u4e45\u6ca1\u6709\u66f4\u65b0\u5fae\u535a\u4e86\uff0c\u54ea\u6015\u8fde\u751f\u6d3b\u7684\u70b9\u6ef4\u90fd\u5e38\u5e38\u5fd8\u8bb0\u8dd1\u5230\u8fd9\u7eaa\u5f55\u3002\u6709\u4e86\u667a\u80fd\u624b\u673a\uff0c\u6709\u4e86\b\u670b\u53cb\u5708\uff0c\u4f3c\u4e4e\u5df2\u7ecf\u5fd8\u8bb0\u6709\u535a\u5ba2\u8fd9\u4ef6\u4e8b\u60c5\u4e86\u3002\u5076\u5c14\u56de\u5230\u8fd9\u91cc\uff0c\u770b\u770b\uff0c\u60f3\u60f3\u3002\u627e\u627e\u8ff7\u5931\u7684\u81ea\u5df1\uff0c\u53d1\u73b0\uff0c\u4e00\u5207\u90fd\u8fd8\u662f\u90a3\u4e48\u53ef\u7231\uff0c\u4e00\u5207\u90fd\u8fd8\u662f\u4eff\u4f5b\u53d1\u751f\u5728\u6628\u5929\u3002<\/font><\/p>","view_time":"556","reply_time":"2","image_path":"","lastpost":"2015-06-08 02:38:27","url":"","categories":"16","pubDate":"1431773158","category":"Life"},{"id":"125","publishtime":"2014-01-16 06:38:08","title":"2014\u6765\u5f97\u5306\u5fd9\uff0c2013\u8d70\u5f97\u7d27\u5f20","author":"YouYee","email":"youyee@youyee.org","content":"<p align=\"left\"><font face=\"Verdana\" color=\"#000000\">\u56de\u770b13\u5e74\uff0c\u906d\u9047\u4e86\u4eba\u751f\u3001\u4e8b\u4e1a\u4e0a\u7684\u5f88\u591a\u53d8\u52a8\u3002<\/font><\/p><p align=\"left\"><font face=\"Verdana\" color=\"#000000\">\u611f\u8c22\u90a3\u4e9b\u966a\u4f34\u6211\u8d70\u8fc7\u5982\u6b64\u4e0d\u5bb9\u6613\u7684\u4e00\u5e74\u7684\u4eba\u3002<\/font><\/p>","view_time":"819","reply_time":"0","image_path":"","lastpost":"2014-01-16 06:41:22","url":"","categories":"12","pubDate":"1389879488","category":"Comment World"}]
[{"id":"124","publishtime":"2013-08-31 10:24:50","title":"\u6211\u7684\u7237\u7237","author":"YouYee","email":"youyee@youyee.org","content":"<p align=\"left\"><font face=\"Verdana\" color=\"#000000\">\u66f4\u65b0\u4e8e2015\u5e748\u67083\u65e5     <\/font><\/p><p align=\"left\"><font face=\"Verdana\" color=\"#000000\">    \u7237\u7237\u79bb\u5f00\u6211\u4eec\u5feb\u4e24\u5e74\u4e86\uff0c\u73b0\u5728\u4f9d\u65e7\u4f1a\u5728\u665a\u4e0a\u505a\u68a6\uff0c\u68a6\u89c1\u7237\u7237\u3002\u5728\u68a6\u4e2d\uff0c\u5374\u5f88\u96be\u770b\u6e05\u695a\u7237\u7237\u7684\u8138\uff0c\u603b\u662f\u62c5\u5fc3\u7237\u7237\u7684\u8eab\u4f53\u3002<\/font><\/p><p align=\"left\"><font face=\"Verdana\" color=\"#000000\">\t\u7237\u7237\u51fa\u8eab\u5728\u4e00\u4e2a\u8d2b\u5bd2\u7684\u5bb6\u5ead\uff0c\u5b66\u4e60\u523b\u82e6\uff0c\u8bfb\u4e86\u5927\u5b66\uff0c\u6210\u4e3a\u4e86\u4e00\u540d\u519b\u533b\u3002\u53c2\u52a0\u8fc7\u8fdc\u5f81\u519b\uff0c\u8fdb\u5165\u8fc7\u671d\u9c9c\u6218\u573a\uff0c\u5728\u4e1c\u4e09\u7701\u548c\u9752\u6d77\u90fd\u5e26\u8fc7\u533b\u7597\u961f\u3002\u8f6c\u4e1a\u540e\u5728\u5730\u533a\u533b\u9662\u5f53\u4e86\u533b\u751f\u4e3b\u4efb\uff0c\u540e\u6765\u5f53\u4e86\u533b\u9662\u9662\u957f\u3002\u7237\u7237\u751f\u6d3b\u8282\u4fed\u6e05\u5ec9\uff0c\u542c\u5976\u5976\u8bf4\u4ee5\u524d\u522b\u4eba\u9001\u6211\u7237\u7237\u4e00\u53ea\u9e21\u3001\u4e00\u58f6\u6cb9\uff0c\u4ed6\u6536\u4e0b\u540e\u90fd\u662f\u7b97\u597d\u94b1\u62ff\u56de\u7ed9\u4eba\u5bb6\u3002\u90a3\u4e2a\u65f6\u5019\u56e0\u4e3a\u7ecf\u5386\u4e86\u6587\u9769\uff0c\u7ecf\u5386\u5404\u79cd\u653f\u6cbb\u8fd0\u52a8\uff0c\u843d\u4e0b\u4e86\u80c3\u75c5\uff0c\u56e0\u4e3a\u80c3\u51fa\u8840\uff0c\u540e\u6765\u505a\u4e86\u80c3\u90e8\u8fdc\u7aef\u5207\u9664\u624b\u672f\uff0c\u56e0\u6b64\u6bcf\u9910\u4e0d\u80fd\u5403\u592a\u591a\u7684\u4e1c\u897f\u3002<\/font><\/p><p align=\"left\"><font face=\"Verdana\" color=\"#000000\">\t\u5c0f\u7684\u65f6\u5019\uff0c\u8bb0\u5f97\u7237\u7237\u8fd8\u8ddf\u6211\u4eec\u4f4f\u5728\u4e00\u8d77\uff0c\u7ecf\u5e38\u8bf4\u7535\u98ce\u6247\u5377<\/font><\/p><p align=\"left\"><font face=\"Verdana\" color=\"#000000\">\u5377\u5377\uff08\u201c\u8f6c\u8f6c\u8f6c\u201d\uff0c\u7237\u7237\u6709\u5f88\u91cd\u7684\u4e61\u97f3\uff09\u9017\u6211\u73a9\u3002\u5c0f\u65f6\u5019\u4e0d\u613f\u610f\u53bb\u5e7c\u513f\u56ed\uff0c\u7237\u7237\u603b\u662f\u8bf4\u4ed6\u9001\u6211\u53bb\u3002\u5f53\u65f6\u6211\u4eec\u4f4f\u7684\u5e73\u623f\uff0c\u7237\u7237\u5728\u9662\u5b50\u91cc\u517b\u4e86\u9e21\uff0c\u8fd8\u79cd\u4e86\u8461\u8404\u3001\u65e0\u82b1\u679c\u3001\u77f3\u69b4\u3001\u6708\u5b63\u82b1\u3002\u5c0f\u65f6\u5019\uff0c\u90a3\u9662\u5b50\u7b80\u76f4\u662f\u6211\u73a9\u4e50\u7684\u5929\u5802\u3002\u8bb0\u5f97\u4ee5\u524d\u7237\u7237\u79cd\u7684\u8461\u8404\uff0c\u5728\u7ed3\u6ee1\u679c\u7684\u65f6\u5019\uff0c\u8001\u662f\u6709\u5916\u9762\u7684\u5c0f\u5b69\u5077\u5077\u722c\u5899\u6765\u6458\u6211\u4eec\u5bb6\u7684\u8461\u8404\u3002<\/font><\/p>","view_time":"986","reply_time":"0","image_path":"201373123289890.jpg","lastpost":"2016-06-15 09:30:27","url":"","categories":"16","pubDate":"1377966290","category":"Life"},
{"id":"123","publishtime":"2013-01-24 11:28:21","title":"\u5199\u5728\u8fd9\u5931\u7720\u7684\u591c","author":"YouYee","email":"youyee@youyee.org","content":"<p align=\"left\"><font face=\"Verdana\" color=\"#000000\">\u8f6c\u773c\u5df2\u7ecf\u5230\u4e862013\u5e74\uff0c\u5730\u7403\u8fd8\u5728\uff0c\u6211\u4e5f\u8fd8\u5728\u3002<\/font><\/p><p align=\"left\"><font face=\"Verdana\" color=\"#000000\">\u65f6\u95f4\u8fc7\u5f97\u5f88\u5feb\uff0c\u8fd9\u4e00\u5e74\uff0c\u5f88\u5fd9\uff0c\u5f88\u7d2f\uff0c\u6536\u83b7\u548c\u5931\u53bb\u7684\u90fd\u633a\u591a\uff0c\u6709\u7684\u65f6\u5019\u611f\u89c9\u5c31\u50cf\u547d\u8fd0\u5728\u4e0d\u65ad\u5730\u548c\u6211\u5f00\u7740\u73a9\u7b11\uff0c\u8ba9\u6211\u7ecf\u5386\u7740\u4ed6\u8bbe\u5b9a\u597d\u7684\u66f2\u6298\u7684\u5267\u672c\u3002\u8fd9\u4e00\u5e74\uff0c\u5982\u6211\u6240\u613f\uff0c\u6211\u5b8c\u5b8c\u5168\u5168\u53d8\u6210\u4e86\u4e00\u4e2a\u7ec8\u7aef\u5f00\u53d1\uff0c\u4eceObjective C\u5230C\uff0c\u4eceSQLite\u5230CoreData\uff0c\u4e00\u5207\u90fd\u5728\u53d8\uff0c\u8fc5\u901f\u7684\u671d\u7740\u67d0\u4e2a\u4e0d\u786e\u5b9a\u7684\u65b9\u5411\u5728\u53d8\u3002\u516c\u53f8\u4ece\u4e0a\u5230\u4e0b\u90fd\u5728\u8bf4\u79fb\u52a8\u9769\u547d\uff0c\u53ef\u662f\u5374\u9c9c\u6709\u51e0\u4e2a\u56e2\u961f\u80fd\u771f\u6b63\u505a\u51fa\u51fa\u8272\u7684\u4ea7\u54c1\u3002\u90a3\u4e9b\u7ecf\u7406\u4eec\uff0c\u603b\u76d1\u4eec\uff0c\u5929\u5929\u5728\u60f3\u7740\u600e\u4e48\u4ece\u79fb\u52a8\u5e02\u573a\u5206\u4e00\u676f\u7fb9\uff0c\u56de\u770b\u53bb\u5e74\u4e00\u6574\u5e74\uff0c\u5230\u73b0\u5728\u90fd\u5f88\u96be\u56de\u8fc7\u795e\u6765\u3002<\/font><\/p>","view_time":"1310","reply_time":"3","image_path":"","lastpost":"2013-04-21 21:02:57","url":"","categories":"16","pubDate":"1359052101","category":"Life"}]

[{"id":"122","publishtime":"2012-04-29 01:00:58","title":"2012, \u5982\u679c\u4e0d\u662f\u4e16\u754c\u672b\u65e5","author":"YouYee","email":"youyee@youyee.org","content":"<p align=\"left\"><font face=\"Verdana\" color=\"#000000\">\u8f6c\u773c\u5230\u4e86\u65b0\u7684\u4e00\u5e74, \u56e0\u4e3a\u5fd9, \u56e0\u4e3a\u516c\u53f8\u91cc\u9762\u7684\u9879\u76ee, \u4e5f\u56e0\u4e3a\u6280\u672f\u4e0a\u7684\u8f6c\u578b, \u535a\u5ba2\u5f88\u4e45\u6ca1\u6709\u66f4\u65b0\u4e86, \u4e58\u7740\u4eca\u5929\u96be\u5f97\u7684\u7a7a\u95f2, \u5077\u5077\u4e0a\u6765\u5199\u4e00\u7bc7\u6587\u7ae0\u5427.<\/font><\/p><p align=\"left\"><font face=\"Verdana\" color=\"#000000\">\u81ea\u4ece\u6bd5\u4e1a\u5230\u73b0\u5728, \u611f\u89c9\u5728\u516c\u53f8\u505a\u4e86\u5f88\u591a\u9879\u76ee, \u5374\u5f88\u96be\u505a\u5230\u4e00\u4e2a\u9879\u76ee\u6709\u59cb\u6709\u7ec8, \u8fd9\u4f30\u8ba1\u662f\u81ea\u5df1\u4ece\u4e1a\u4ee5\u6765\u6700\u5927\u7684\u9057\u61be\u5427. \u4ece\u521a\u8fdb\u516c\u53f8\u8d1f\u8d23\u5f00\u53d1\u7ef4\u62a4Qzone\u524d\u7aef, \u5230\u540e\u53f0\u505aQQ\u9910\u5385, QQ\u8d85\u5e02, QQ\u4fa0\u76d7, \u4ee5\u53ca\u77ed\u6682\u7684\u5f00\u653e\u5e73\u53f0\u518d\u5230\u76ee\u524d\u7684QQ\u95f9\u949f, \u7ecf\u5386\u4e86\u5f88\u591a\u5f88\u591a, \u5374\u611f\u89c9\u4e00\u76f4\u6ca1\u6709\u4f5c\u51fa\u4e00\u4e2a\u8ba9\u81ea\u5df1\u5fc3\u7406\u6ee1\u8db3\u7684\u4ea7\u54c1. \u6211\u60f3\u6211\u8fd8\u662f\u4e00\u4e2a\u4e0d\u4ec5\u4ec5\u60f3\u53ea\u505a\u6280\u672f\u7684\u5f00\u53d1\u5427.<\/font><\/p>","view_time":"2120","reply_time":"3","image_path":"","lastpost":"2012-10-29 05:50:53","url":"","categories":"16","pubDate":"1335682858","category":"Life"},{"id":"121","publishtime":"2011-06-25 18:58:22","title":"\u4e0d\u5efa\u8bae\u4f7f\u7528Flash\u5f00\u53d1\u590d\u6742\u7684iOS\u6e38\u620f","author":"YouYee","email":"youyee@youyee.org","content":"<p align=\"left\"><font face=\"Verdana\" color=\"#000000\">\u81ea\u4ece Adobe \u63a8\u51fa iOS Packager \u540e, \u5f88\u591aFlash \u5f00\u53d1\u90fd\u96c0\u8dc3\u6b32\u8bd5, \u7136\u800c\u73b0\u5b9e\u4e2d \u4f1a\u9047\u5230\u5f88\u591a\u95ee\u9898. \u5728\u8fd9\u91cc\u5206\u4eab\u4e0b.<\/font><\/p><p align=\"left\"><font face=\"Verdana\" color=\"#000000\"><\/font><\/p>","view_time":"4880","reply_time":"3","image_path":"","lastpost":"2012-04-29 00:42:36","url":"","categories":"9","pubDate":"1309049902","category":"RIA Develop"}]
[{"id":"120","publishtime":"2010-05-31 02:32:30","title":"\u54c0\u5176\u4e0d\u5e78\uff0c\u6012\u5176\u4e0d\u4e89","author":"YouYee","email":"youyee@youyee.org","content":"<p align=\"left\"><font face=\"Verdana\" color=\"#000000\">    \u4ece\u6807\u9898\u5c31\u770b\u51fa\u6765\u8fd9\u662f\u4e00\u7bc7\u9644\u5e26\u5f3a\u70c8\u4e2a\u4eba\u611f\u60c5\u8272\u5f69\u7684\u6587\u7ae0\uff0c\u800c\u8fd9\u4e2a\u6807\u9898\u6240\u63cf\u8ff0\u7684\u5bf9\u8c61\u5c31\u662f\u2014\u2014Flash\u3002<\/font><\/p><p align=\"left\"><font face=\"Verdana\" color=\"#000000\"><\/font><\/p><p align=\"left\"><font face=\"Verdana\" color=\"#000000\">    \u5148\u4ece\u6211\u81ea\u5df1\u7684\u7ecf\u5386\u5f00\u59cb\u4ecb\u7ecd\u5427\uff0c\u4ece\u9ad8\u4e2d\u5f00\u59cb\u5c31\u63a5\u89e6Flash 5\u4e00\u76f4\u5230\u73b0\u5728\uff0c\u6211\u9664\u4e86\u4e2d\u95f4\u4e2d\u65ad\u4e86\u63a5\u8fd1\u4e24\u5e74\u7684\u65f6\u95f4\u4ece\u4e8bJavaScript\u5f00\u53d1\uff0c\u8fd9\u4e03\u5e74\u6765\u51e0\u4e4e\u90fd\u5728\u56f4\u7740Flash\u6253\u8f6c\u3002\u5728\u6211\u6bd5\u4e1a\u524d\u4e00\u5e74\uff0c\u6211\u5f00\u59cb\u7740\u624bJavaScript\u65b9\u9762\u7684\u5f00\u53d1\uff0c\u76f4\u5230\u6bd5\u4e1a\u540e\u4e00\u5e74\u4e5f\u662f\u4e00\u76f4\u4ece\u4e8bJavaScript\u5f00\u53d1\uff0c\u671f\u95f4\u4f9d\u65e7\u6ca1\u6709\u653e\u5f03\u8fc7Flash\uff0c\u53ea\u662f\u5de5\u4f5c\u4e0a\u66f4\u52a0\u504f\u91cd\u4e0eJavaScript\u3002\u523009\u5e74\u5e95\uff0c\u56e0\u4e3a\u5de5\u4f5c\u9700\u8981\uff0c\u6211\u53c8\u7ee7\u7eed\u56de\u5230\u4e86Flash\u5f00\u53d1\u8fd9\u4e2a\u804c\u4e1a\u89d2\u8272\u3002<\/font><\/p><p align=\"left\"><font face=\"Verdana\" color=\"#000000\"><\/font><\/p><p align=\"left\"><font face=\"Verdana\" color=\"#000000\">    \u4eceFlash 5\u4e00\u8def\u8d70\u6765\uff0cFlash\u7ed9\u6211\u4eec\u5f00\u53d1\u8005\u5e26\u6765\u4e86\u4e00\u6b21\u53c8\u4e00\u6b21\u7684\u60ca\u559c\uff0c\u4e5f\u5e26\u6765\u4e86\u4e00\u6b21\u53c8\u4e00\u6b21\u7684\u5931\u671b\uff0c\u6211\u4eec\u770b\u5230\u4e86Flash\u7684\u8fdb\u6b65\uff0c\u4f46\u662f\u4e5f\u770b\u5230\u4e86Flash\u7684\u5c40\u9650\u548c\u4e0d\u8db3\u3002\u5c24\u5176\u662f\u6700\u8fd1Apple\u5904\u4e8e\u81ea\u8eab\u5229\u76ca\u5bf9Flash\u7684\u6279\u5224\u66f4\u52a0\u5c06Flash\u63a8\u5230\u4e86\u98ce\u5934\u6d6a\u5c16\u4e0a\uff0c\u6211\uff0c\u505a\u4e3a\u4e00\u4e2a\u5f00\u53d1\u8005\u6765\u8c08\u8c08\u81ea\u5df1\u5bf9Flash\u7684\u611f\u53d7\u5427\u3002<\/font><\/p><p align=\"left\"><font face=\"Verdana\" color=\"#000000\"><\/font><\/p><p align=\"left\"><font face=\"Verdana\" color=\"#000000\">     Flash Player\u4f5c\u4e3a\u4e00\u4e2a\u81ea\u79f0\u80fd\u8de8\u6d4f\u89c8\u5668\u63d0\u4f9b\u4f53\u9a8c\u4e00\u81f4\u7684\u5e73\u53f0\uff0c\u5728\u5f88\u591a\u65f6\u5019\u90fd\u662f\u88ab\u7528\u6765\u5448\u73b0\u56fe\u8868\uff0c\u7528\u4e8e\u63d0\u4f9b\u76f8\u5bf9\u4e8eHTML + JavaScript\u66f4\u52a0\u4e30\u5bcc\u4f53\u9a8c\u7f51\u9875\u5e94\u7528\u7a0b\u5e8f\uff0c\u6bd4\u5982\u6570\u636e\u56fe\u8868\u548c\u56fe\u7247\u7f16\u8f91\u7b49\uff0cFlash\u5728\u5927\u591a\u6570\u60c5\u51b5\u4e0b\u90fd\u80fd\u63d0\u4f9b\u6bd4\u8f83\u597d\u7684\u4f53\u9a8c\uff0c\u800c\u4e14\u5408\u7406\u7684\u5c06\u754c\u9762\u548c\u903b\u8f91\u5206\u79bb\u6210SWC\u4e0eAS\uff0c\u4ece\u5f00\u53d1\u4f53\u9a8c\u4e0a\u4e5f\u8fd8\u7b97\u6bd4\u8f83\u5408\u7406\uff0c\u5728PC\u5e73\u53f0\u4e0a\uff0cFlash\u81f3\u5c11\u5728\u76ee\u524d\u800c\u8a00\u8fd8\u662f\u975e\u5e38\u597d\u7528\u7684\u3002<\/font><\/p>","view_time":"4611","reply_time":"11","image_path":"","lastpost":"2011-11-28 02:45:21","url":"","categories":"5","pubDate":"1275294750","category":"Ajax & Flash"},{"id":"119","publishtime":"2010-03-06 08:53:37","title":"HTML5\u548cFlash\uff0c\u4e0d\u662f\u4f60\u6b7b\u5c31\u662f\u6211\u6d3b\uff1f","author":"YouYee","email":"youyee@youyee.org","content":"<p align=\"left\"><font face=\"Verdana\" color=\"#000000\">     \u6700\u8fd1HTML5\u548cFlash\u88ab\u7092\u5f97\u6cb8\u6cb8\u626c\u626c\uff0cAdobe\u548cApple\u4e4b\u95f4\u7684\u5bf9\u9a82\u4e5f\u5341\u5206\u6709\u610f\u601d\uff0c\u4f5c\u4e3a\u4e00\u4e2a\u5f00\u53d1\u8005\u7684\u4f60\u7279\u522b\u662f\u4ece\u4e1a\u4e0eFlash\u5f00\u53d1\u7684\u4f60\u6709\u8003\u8651\u8fc7\u5417\uff1f<\/font><\/p><p align=\"left\"><font face=\"Verdana\" color=\"#000000\">     \u5c31\u6211\u672c\u8eab\u800c\u8a00\uff0c\u6211\u867d\u7136\u5f88\u7231Flash\uff0c\u6bd5\u7adf\u8fd9\u662f\u6211\u4e00\u76f4\u90fd\u5f88\u559c\u6b22\u73a9\u7684\u4e00\u4e2a\u5e73\u53f0\uff0c\u5728MM\u65f6\u4ee3\uff0cFlash\u7ed9\u4eba\u5e26\u6765\u4e00\u6b21\u53c8\u4e00\u6b21\u7684\u60ca\u559c\uff0c\u6211\u751a\u81f3\u65e0\u6cd5\u5fd8\u8bb0\u6bcf\u6b21Flash\u66f4\u65b0\u7ed9\u5f00\u53d1\u8005\u5e26\u6765\u559c\u60a6\u7684\u573a\u666f\uff0c\u6bcf\u6b21\u5728Adobe Labs \u4e0a\u770b\u5230\u65b0\u7684\u7248\u672c\u63a8\u51fa\u7684\u65f6\u5019\uff0c\u603b\u662f\u7b2c\u4e00\u65f6\u95f4\u53bb\u4e86\u89e3\u7a76\u7adf\u591a\u4e86\u54ea\u4e9b\u529f\u80fd\uff0c\u4ece\u8fd9\u4e9b\u65b0\u529f\u80fd\u4e2d\u80fd\u6709\u90a3\u4e9b\u80fd\u7ed9\u81ea\u5df1\u7684\u5f00\u53d1\u5e26\u6765\u5e2e\u52a9\uff0c\u6211\u51e0\u4e4e\u5e9f\u5bdd\u5fd8\u98df\u7684\u53bb\u5b66\u4e60\u53bb\u7814\u7a76\u8fd9\u4e9b\u4e1c\u897f\u3002<\/font><\/p><p align=\"left\"><font face=\"Verdana\" color=\"#000000\">     \u7136\u800c\u4e0d\u5f97\u4e0d\u627f\u8ba4\uff0c\u8fd9\u4e00\u5e74\uff0cAdobe\u7ed9\u6211\u5e26\u6765\u4e86\u4e00\u6b21\u53c8\u4e00\u6b21\u7684\u5931\u671b\uff0c\u5b89\u5168\u6f0f\u6d1e\u65b9\u9762\u7684\u95ee\u9898\u5c31\u4e0d\u8bf4\u4e86\uff0c\u5728Mac\u4e0b\uff0c\u6267\u884c\u6548\u7387\u4e00\u76f4\u5f88\u5dee\uff0810.1\u636e\u8bf4\u597d\u4e86\u5f88\u591a\uff09\uff1b\u6240\u8c13\u7684\u591a\u5e73\u53f0\u6700\u7ec8\u4f9d\u65e7\u6ca1\u80fd\u591f\u5728iPhone\u4e0a\u5f97\u5230\u652f\u6301\uff0c\u751a\u81f3\u5bf9\u4e8e\u6444\u50cf\u5934\u7684\u8fde\u63a5\u4f60\u90fd\u8981\u9488\u5bf9\u5e73\u53f0\u53bb\u5199\u7279\u6b8a\u7684\u903b\u8f91\uff1b\u6700\u7cdf\u7cd5\u7684\u662fFlash IDE\uff0c\u81c3\u80bf\uff0c\u6548\u7387\u5e95\u4e0b\uff0c\u62e5\u67092G\u5185\u5b58\u7684\u673a\u5668\u8dd1CS4\u4f9d\u65e7\u5341\u5206\u5403\u529b\u3002<\/font><\/p><p align=\"left\"><font face=\"Verdana\" color=\"#000000\">    \u56de\u5934\u518d\u770b\u770b\u6d4f\u89c8\u5668\u7684\u53d1\u5c55\uff0cSafari\uff0cChrome\uff0cFirefox\u90fd\u5f00\u59cb\u652f\u6301HTML5\uff0c\u65b0\u4e00\u4ee3\u6d4f\u89c8\u5668\u5f00\u59cb\u652f\u6301OpenGL\u6216\u8005\u5176\u4ed6\u7684\u786c\u4ef6\u52a0\u901f\uff0cCSS3\u6b63\u5728\u5411\u5f00\u53d1\u8005\u8d70\u6765...\u4f60\u53ef\u80fd\u4f1a\u4e0d\u5c51\u4e00\u987e\u7684\u8bf4\uff1aIE6\u4e00\u65e5\u4e0d\u6b7b\u5c31\u522b\u548c\u6211\u8c08\u53d6\u4ee3Flash\uff0c\u4f5c\u4e3a\u4e00\u4e2aFlash\u7231\u597d\u8005\uff0c\u4f60\u53ef\u4ee5\u6548\u5fe0\u4e8e\u4f60\u7684\u5e73\u53f0\uff0c\u751a\u81f3\u5305\u5bb9\u4ed6\u6240\u6709\u7684\u7f3a\u70b9\uff0cFlash\u5f88\u5f3a\u5927\uff0c\u5f3a\u5927\u5230\u51e0\u4e4e\u6240\u6709\u95ee\u9898\u90fd\u80fd\u89e3\u51b3\uff0c\u53ea\u662f\u6bd4\u8f83\u68d8\u624b\u800c\u5df2\u3002\u53ef\u662f\u4e0d\u8981\u5fd8\u8bb0\uff0cFlash\u662f\u5bc4\u751f\u4e8e\u6d4f\u89c8\u5668\uff0c\u5982\u679c\u6ca1\u6709HTML, \u751a\u81f3\u8fde\u5d4c\u5165\u7f51\u9875\u7684\u673a\u4f1a\u90fd\u6ca1\u6709\uff0c\u6211\u4eec\u603b\u662f\u5728\u8bf4Flash Player\u666e\u53ca\u7684\u901f\u5ea6\u5f88\u5feb\uff0c\u4f46\u662f\u6211\u4eec\u8003\u8651\u5230\u4e86\u7f51\u5427\u7528\u6237\u5417\uff1f\u4ed6\u4eec\u7684\u673a\u5668\u4e0a\u662f\u88c5\u6709\u8fd8\u539f\u5361\uff0c\u8fd9\u610f\u5473\u7740\u4ed6\u4eec\u5173\u673a\u540e\u6240\u6709\u7684\u66f4\u65b0\u90fd\u88ab\u91cd\u7f6e\uff0cFlash\u7ec8\u7a76\u662f\u4e00\u4e2a\u63d2\u4ef6\u3002<\/font><\/p><p align=\"left\"><font face=\"Verdana\" color=\"#000000\">     \u8bb0\u5f97\u4ee5\u524dLuar\u5199\u8fc7\u4e00\u7bc7\u6587\u7ae0\u300a<font color=\"#93C400\"><a href=\"http:\/\/www.luar.com.hk\/flashbook\/archives\/001317.php\" target=\"_blank\"><u>Flash\u7684\u672a\u6765\u672a\u6709\u6765<\/u><\/a><\/font>\u300b\uff0c\u4ed6\u7684\u9884\u8a00\u4f3c\u4e4e\u6ca1\u6709\u4efb\u4f55\u504f\u5dee\uff0cFlash\u5728RIA\u5e94\u7528\u4e0a\u88abAjax\u62a2\u53bb\u4e86\u98ce\u5934\uff0c\u7cdf\u7cd5\u7684\u53ef\u7528\u6027\u548c\u5dee\u52b2\u7684\u6587\u672c\u5448\u73b0\u80fd\u529b\u5bfc\u81f4Flash\u5728\u8fd9\u4e2a\u9886\u57df\u8282\u8282\u8d25\u9000\u3002\u6211\u662f\u4e00\u4e2aFlash\u804c\u4e1a\u5f00\u53d1\uff0c\u540c\u65f6\u4e5f\u662f\u4e00\u4e2aFrontEnd \u804c\u4e1a\u5f00\u53d1\uff0c\u4e0d\u4f1a\u504f\u8892\u4efb\u4f55\u4e00\u65b9\uff0c\u53ea\u662f\u6211\u610f\u8bc6\u5230\u73b0\u5728Flash\u7684\u5371\u673a\u6765\u4e86\uff0c\u4e0d\u4ec5\u4ec5\u662fHTML5\uff0c\u4e0d\u4ec5\u4ec5\u662f\u6d4f\u89c8\u5668\u7684\u9769\u547d\u3002<\/font><\/p><p align=\"left\"><font face=\"Verdana\" color=\"#000000\">    \u8ba9\u6211\u4eec\u770b\u770b\u539f\u6765\u5f88\u591a\u4e0d\u5f97\u4e0d\u7528Flash\u5b9e\u73b0\u7684\u529f\u80fd\uff1a<\/font><\/p><p align=\"left\"><font face=\"Verdana\" color=\"#000000\">1\u3001\u6587\u4ef6\u7684\u4e0a\u4f20<\/font><\/p><p align=\"left\"><font face=\"Verdana\" color=\"#000000\">2\u3001\u6444\u50cf\u5934\u62cd\u7167<\/font><\/p><p align=\"left\"><font face=\"Verdana\" color=\"#000000\">3\u3001\u6570\u636e\u56fe\u8868\u663e\u793a<\/font><\/p><p align=\"left\"><font face=\"Verdana\" color=\"#000000\">4\u3001\u5bcc\u542b\u52a8\u611f\u7684\u5c0f\u52a8\u753b<\/font><\/p>","view_time":"5173","reply_time":"11","image_path":"","lastpost":"2012-02-23 21:19:38","url":"","categories":"5","pubDate":"1267890817","category":"Ajax & Flash"}]

'''
