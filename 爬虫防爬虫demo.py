# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

'''

import urllib.request
import re
import urllib.error

url = 'http://blog.csdn.net/'
headers = ("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36")

opener = urllib.request.build_opener()
opener.addheaders = [headers]

# 添加headers到全局
urllib.request.install_opener(opener)

data = urllib.request.urlopen(url=url, timeout=20).read().decode('utf-8', 'ignore')
pat = '"tracking-ad" data-mod="popu_254"><a href="(.*?)"'
result = re.compile(pat).findall(data)

print(result)

for i in range(0, len(result)):
    try:
        file = './a/' + str(i) + '.html'
        urllib.request.urlretrieve(result[i], filename=file)
        print('正在下载%s页' %i)
    except urllib.error as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
'''

# ~~~~~~~~~~~~~~~~~~~~~~~~~~  我是帅气的分割线  ~~~~~~~~~~~~~~~~~~~~~~~~~~


'''

# 使用IP代理
import urllib.request
import urllib.error

def user_proxy(url, proxy_addr):

    try:
        proxy = urllib.request.ProxyHandler({'https': proxy_addr})
        print(dir(proxy))
        print(proxy.proxies)
        print(proxy.handler_order)
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        # 添加到全局
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
        # print(data)
        return data
    except urllib.error as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason + 'ad')

url = 'http://www.baidu.com'
proxy_addr = ['106.127.183.78:61202', "117.87.128.218:61202", "183.20.8.46:61234"]

user_proxy(url, proxy_addr)
'''

# ~~~~~~~~~~~~~~~~~~~~~~~~~~  我是帅气的分割线  ~~~~~~~~~~~~~~~~~~~~~~~~~~



'''


图片爬虫
import urllib.request
import re
import ssl
context = ssl._create_unverified_context()

keyname = '连衣裙'
# 把关键词编码
key = urllib.request.quote(keyname)

# 设置UA
headers = ("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
# 把UA添加到全局
urllib.request.install_opener(opener)

# 遍历每个关键词的页数
for i in range(0, 101):
    url = "https://s.taobao.com/list?q=" + key + "&cat=16&style=grid&seller_type=taobao&spm=a219r.lm874.1000187.1&bcoffset=12&s=" + str(i * 60)
    data = urllib.request.urlopen(url=url, context=context).read().decode('utf-8', 'ignore')

    # 图片re棋盘
    pat = 'pic_url":"//(.*?)"'

    imagelist = re.compile(pat).findall(data)

    # 循环获取img图片url
    for j in range(0, len(imagelist)):
        thisimg = imagelist[i]
        thisimgurl = "http://" + thisimg
        file = './img/' + str(i) + str(j) + '.jpg'

        # 保存图片
        urllib.request.urlretrieve(thisimgurl, filename=file)
        print('保存图片%s成功'% file)

'''

# ~~~~~~~~~~~~~~~~~~~~~~~~~~  我是帅气的分割线  ~~~~~~~~~~~~~~~~~~~~~~~~~~


'''

# 千图网高清图片
import urllib.request
import re
import urllib.error
for i in range(1,10):
    pageurl = 'http://www.58pic.com/tupian/cuxiaohaibao-800-0-' + str(i) +'.html'
    data = urllib.request.urlopen(pageurl).read().decode('utf-8', 'ignore')
    pat = '<div class="card-tag-business "></div><!----></div><img src="(.*?)!'
    imglist = re.compile(pat).findall(data)
    for j in range(0, len(imglist)):
        try:
            thisimg =   imglist[j]
            file = './img/' + str(i) + str(j) + '.jpg'
            urllib.request.urlretrieve(thisimg, filename=file)
            print('保存图片%s->%s成功' % (i, j))

        except urllib.error as e:
            if hasattr(e, 'code'):
                print(e.code)
            if hasattr(e, 'reason'):
                print(e.reason)

'''

# ~~~~~~~~~~~~~~~~~~~~~~~~~~  我是帅气的分割线  ~~~~~~~~~~~~~~~~~~~~~~~~~~



'''
# 抓取腾讯视频评论
import urllib.request
import re
import urllib.error

# 设置UA
headers = ("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)

comid = "6165793094371986503"
url = "http://video.coral.qq.com/filmreviewr/c/upcomment/0dfpyvfa7tp0ewe?commentid=" + comid + "&reqnum=3&callback=jQuery1120026430801920245595_1478436999932&_=1478436999935"
for i in range(0, 100):
    data = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')

    # 获取下一页的id
    patnext = '"last":"(.*?)"'
    nextid = re.compile(patnext).findall(data)[0]
    print(nextid)

    # 获取评论数据
    patcom = '"content":"(.*?)",'
    comdata = re.compile(patcom).findall(data)
    for j in range(0, len(comdata)):
        print('------第' + str(i) + str(j) + '条评论评论内容是: ')
        print(eval('u"' + comdata[j] + '"'))
    url = "http://video.coral.qq.com/filmreviewr/c/upcomment/0dfpyvfa7tp0ewe?commentid=" + nextid + "&reqnum=3&callback=jQuery1120026430801920245595_1478436999932&_=1478436999935"


'''



# ~~~~~~~~~~~~~~~~~~~~~~~~~~  我是帅气的分割线  ~~~~~~~~~~~~~~~~~~~~~~~~~~



'''



# 抓取搜狗微信
import urllib.request
import re
import time
import urllib.error

# 自定义函数, 功能为使用代理服务器抓一个网址
def use_proxy(proxy_addr,url):
    #建立异常处理机制
    try:
        req=urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
        proxy= urllib.request.ProxyHandler({'http':proxy_addr})
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(req).read()
        return data
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        #若为URLError异常，延时10秒执行
        time.sleep(10)
    except Exception as e:
        print("exception:"+str(e))
        #若为Exception异常，延时1秒执行
        time.sleep(1)


#设置关键词
key="Python"
#设置代理服务器，该代理服务器有可能失效，读者需要换成新的有效代理服务器
proxy="219.135.164.245:3128"
#爬多少页
for i in range(0,10):
    key=urllib.request.quote(key)
    thispageurl="http://weixin.sogou.com/weixin?type=2&query="+key+"&page="+str(i)
    #a="http://blog.csdn.net"
    thispagedata=use_proxy(proxy,thispageurl)
    print(len(str(thispagedata)))
    pat1='<a href="(.*?)"'
    rs1=re.compile(pat1,re.S).findall(str(thispagedata))
    if(len(rs1)==0):
        print("此次（"+str(i)+"页）没成功")
        continue
    for  j in range(0,len(rs1)):
        thisurl=rs1[j]
        thisurl=thisurl.replace("amp;","")
        file="./a/第"+str(i)+"页第"+str(j)+"篇文章.html"
        thisdata=use_proxy(proxy,thisurl)
        try:
            fh=open(file,"wb")
            fh.write(thisdata)
            fh.close()
            print("第"+str(i)+"页第"+str(j)+"篇文章成功")
        except Exception as e:
            print(e)
            print("第"+str(i)+"页第"+str(j)+"篇文章失败")
'''



# ~~~~~~~~~~~~~~~~~~~~~~~~~~  我是帅气的分割线  ~~~~~~~~~~~~~~~~~~~~~~~~~~




'''

# 抓取糗事百科
import urllib.request
import re
import urllib.error
import ssl
context = ssl._create_unverified_context()

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"}

for i in range(1,36):
    url="http://www.qiushibaike.com/8hr/page/"+str(i)
    resp = urllib.request.Request(url, headers=headers)
    pagedata=urllib.request.urlopen(resp, context=context).read().decode("utf-8","ignore")
    pat='<div class="content">.*?<span>(.*?)</span>.*?</div>'
    datalist=re.compile(pat,re.S).findall(pagedata)
    for j in range(0,len(datalist)):
        print("第"+str(i)+"页第"+str(j)+"个段子的内容是：")
        print(datalist[j])
'''




# ~~~~~~~~~~~~~~~~~~~~~~~~~~  我是帅气的分割线  ~~~~~~~~~~~~~~~~~~~~~~~~~~


'''

# 多线程的使用
import threading

class A(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in range(0, 10):
            print('我是线程A')


class B(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in range(0, 10):
            print('我是线程B')

t1 = A()
t1.start()

t2 = B()
t2.start()
'''



# ~~~~~~~~~~~~~~~~~~~~~~~~~~  我是帅气的分割线  ~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~  我是帅气的分割线  ~~~~~~~~~~~~~~~~~~~~~~~~~~




import threading
import urllib.request
import re
import urllib.error
import ssl
context = ssl._create_unverified_context()

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"}


class One(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in range(1, 36, 2):
            url = "http://www.qiushibaike.com/8hr/page/" + str(i)
            resp = urllib.request.Request(url, headers=headers)
            try:
                pagedata = urllib.request.urlopen(resp, context=context).read().decode("utf-8", "ignore")
                pat = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
                datalist = re.compile(pat, re.S).findall(pagedata)
                for j in range(0, len(datalist)):
                    print("第" + str(i) + "页第" + str(j) + "个段子的内容是：")
                    print(datalist[j])
            except Exception as e:
                print(e)


class Two(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in range(0, 36, 2):
            url = "http://www.qiushibaike.com/8hr/page/" + str(i)
            resp = urllib.request.Request(url, headers=headers)
            try:
                pagedata = urllib.request.urlopen(resp, context=context).read().decode("utf-8", "ignore")
                pat = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
                datalist = re.compile(pat, re.S).findall(pagedata)
                for j in range(0, len(datalist)):
                    print("第" + str(i) + "页第" + str(j) + "个段子的内容是：")
                    print(datalist[j])
            except Exception as e:
                print(e)

one = One()
one.start()

two = Two()
two.start()
