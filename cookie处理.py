#cookie保存
import urllib.request
import http.cookiejar
#建立cookie处理
cjar=http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)
 
#cookie读取
print(str(cjar))