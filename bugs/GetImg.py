import re
import requests
import random


def spiderPic(html, keyword):
    print('查找 ' + keyword + ' 中......')
    for addr in re.findall('"objURL":"(.*?)"', html, re.S):
        print('获取URL：' + str(addr)[0:30] + '...')

        try:
            pics = requests.get(addr, timeout=10)
        except requests.exceptions.ConnectionError:
            print('URL Error')
            continue
        fq = open('C:\\Users\\Administrator\\Desktop\\cpyProject\\img\\it\\img' + (
                keyword + '_' + str(random.randrange(0, 5000, 4)) + '.jpg'), 'wb')
        fq.write(pics.content)
        fq.close()


if __name__ == '__main__':
    word = input('Key：')
    result = requests.get(
        'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=' + word)

spiderPic(result.text, word)
