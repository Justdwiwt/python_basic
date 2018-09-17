# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

from urllib import request

response = request.urlopen("http://www.tmooc.cn/")
content = response.read().decode('utf-8')
print(content)
