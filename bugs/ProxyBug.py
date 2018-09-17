# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

from urllib import request

proxy_support = request.ProxyHandler({'http': 'http://xx.xx.xx.xx:xx'})
opener = request.build_opener(proxy_support, request.HTTPHandler)
request.install_opener(opener)
content = request.urlopen('http://www.tmooc.cn/').read().decode('utf-8')
print(content)
