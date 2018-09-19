# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

import chardet
import requests

data = requests.get('http://www.baidu.com')
charset = chardet.detect(data.content)
print(chardet)
data.encoding = charset['encoding']
print(data.text)
