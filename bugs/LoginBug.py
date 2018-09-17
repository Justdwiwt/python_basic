# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

from urllib import parse, request

# noinspection SpellCheckingInspection
postdata = parse.urlencode({
    'username': 'xxx',
    'password': 'xxx',
    'continueURI': 'http://www.tmooc.cn/',
    'fk': 'fkasdfasdf',
    'login_submit': '登录',
})

req = request.Request(
    url='http://www.tmooc.cn/',
    data=postdata
)
content = request.urlopen(req).read()
print(content)
