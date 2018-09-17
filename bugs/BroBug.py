# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

from urllib import parse, request

postdata = parse.urlencode({})
headers = {
    'User-Agent': 'Mozilla/5.0(Windows;U;Windows NT 6.1;en-US;rv:1.9.1.6)'
                  'Gecko/20091201 Firefox/3.5.6'
}
req = request.Request(
    url='http://www.tmooc.cn/',
    data=postdata,
    headers=headers
)
