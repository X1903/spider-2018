# coding=utf-8
# 对js做简单的转化以后,发现继续转化python很复杂,想到一个简单的方法,
# 自己定义类实现一些js的方法

class JsStr(str):

    def substr(self, min, max=None):
        if max:
            return self[min:max]
        else:
            return self[min:]

    def charCodeAt(self, i):
        return ord(self[i])
