# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

import datetime

if __name__ == '__main__':
    dt = datetime.datetime.now()
    print('当前时间：', dt)
    print('(%Y-%m-%d%H:%M:%S%f):', dt.strftime('%Y-%m-%d-%H:%M:%S%f'))
    print('(%Y-%m-%d%H:%M:%S%p):', dt.strftime('%Y-%m-%d-%I:%M:%S%p'))
    print('%%a:%s' % dt.strftime('%a'))
    print('%%A:%s' % dt.strftime('%A'))
    print('%%b:%s' % dt.strftime('%b'))
    print('%%B:%s' % dt.strftime('%B'))
    print('日期时间%%c:%s' % dt.strftime('%c'))
    print('日期%%x:%s' % dt.strftime('%x'))
    print('时间%%X:%s' % dt.strftime('%X'))
    print('今天是这周的第%s天' % dt.strftime('%w'))
    print('今天是今年的第%s天' % dt.strftime('%j'))
    print('今天是今年的第%s周' % dt.strftime('%U'))
