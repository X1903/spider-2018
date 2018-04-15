import urllib.request
import re
import time
key="机器学习"
key=urllib.request.quote(key)
name="微信爬虫_"+str(key)
thisapi='http://api.xdaili.cn/xdaili-api//privateProxy/getDynamicIP/DD2018441370oHHXnN/7331fb7c2eac11e8bcaf7cd30abda612?returnType=1'
for i in range(0,100):
    from uaip3 import *
    thispageurl="http://weixin.sogou.com/weixin?oq=&query="+key+"&type=2&page="+str(i+1)+"&ie=utf8"
    if(i%3==0 and i==0):
        ippools,thispagedata=ua_ip(0,thispageurl,thisapi)
    elif(i%3==0):
        print("正在延时中…")
        time.sleep(15)
        print("延时完成，正在调取IP")
        ippools,thispagedata=ua_ip(0,thispageurl,thisapi)
        print("IP调取完成")
    else:
        ippools,thispagedata=ua_ip(ippools,thispageurl,thisapi)
    print(thispageurl)
    print(len(thispagedata))
    pat1='<div class="txt-box">.*?href="(.*?)"'
    rst1=re.compile(pat1,re.S).findall(thispagedata)
    if(len(rst1)==0):
        print("这一页没有爬成功")
        continue
    for j in range(0,len(rst1)):
        thisurl=rst1[j]
        pat2='amp;'
        thisurl=thisurl.replace(pat2,"")
        print(thisurl)
        ippools,thisdata=ua_ip(ippools,thisurl,thisapi)
        print("这篇文章爬取成功，长度为：" +str(len(thisdata)))
        fh=open("D:/我的教学/Python/天善智能-爬虫/4/微信文章数据/"+str(i)+str(j)+".html","w",encoding="utf-8")
        fh.write(thisdata)
        fh.close()
