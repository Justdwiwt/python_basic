# -*- coding:utf-8 -*-

from lxml import etree
import requests
import re


# from Class.store_csv import CSV


class Spider(object):
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 "
                      "Safari/537.36 "
    }
    cookies = {
        'UM_distinctid': '15ac11bdff316-0ce09a4511f531-67f1a39-100200-15ac11bdff447d',
        'CNZZDATA1258679142': '1034687255-1492307094-%7C1493259066',
        'remember_user_token': 'W1s1MjA4MDY0XSwiJDJhJDEwJFVWVjUwbXBsS1hldkc1d0l3UG5DSmUiLCIxNDk0ODkyNTg0LjczNDM2ODgiXQ%3D%3D--f04b34c274980b45e5f7ee17c2686aeb4b567197',
        '_gat': '1',
        '_session_id': 'N0tvclN3V09wZ25UNFloZ0NrRTBVT3ZYQUR5VkRlV1c2Tno1bnNZc3dmQm9kQ3hmOGY4a0dFUlVLMDdPYWZJdCsydGJMaENZVU1XSHdZMHozblNhUERqaldYTHNWYXVPd2tISHVCeWJtbUFwMjJxQ3lyU2NZaTNoVUZsblV4Si94N2hRRC94MkJkUjhGNkNCYm1zVmM0R0ZqR2hFSFltZnhEcXVLbG54SlNSQU5lR0dtZ2MxOWlyYWVBMVl1a1lMVkFTYS8yQVF3bGFiR2hMblcweTU5cnR5ZTluTGlZdnFKbUdFWUYzcm9sZFZLOGduWFdnUU9yN3I0OTNZbWMxQ2UvbU5aQnByQmVoMFNjR1NmaDJJSXF6WHBYQXpPQnBVRVJnaVZVQ2xUR1p4MXNUaDhQSE80N1paLzg0amlBdjRxMU15a0JORlB1YXJ4V2g0b3hYZXpjR1NkSHVVdnA2RkgvVkJmdkJzdTg5ODhnUVRCSnN2cnlwRVJvWWc4N0lZMWhCMWNSMktMMWNERktycE0wcHFhTnYyK3ZoSWFSUFQzbkVyMDlXd2d5bz0tLThrdXQ2cFdRTTNaYXFRZm5RNWtYZUE9PQ%3D%3D--bc52e90a4f1d720f4766a5894866b3764c0482dd',
        '_ga': 'GA1.2.1781682389.1492310343',
        '_gid': 'GA1.2.163793537.1495583991',
        'Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068': '1495360310,1495416048,1495516194,1495583956',
        'Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068': '1495583991'
    }
    params = []

    def __init__(self):
        field = ['标题', '作者', '发表时间', '阅读量', '评论数', '点赞数', '打赏数', '所投专题']
        # self.write = CSV('main.csv', field)

    def totalPage(self):
        for i in range(1, 16):
            data = '&'.join(self.params)
            url = 'http://www.jianshu.com/?' + data + '&page={}'.format(i)
            self.getData(url)

    def getData(self, url):
        print
        url
        html = requests.get(url, headers=self.headers, cookies=self.cookies).text
        response = etree.HTML(html)
        ids = response.xpath('//*[@id="list-container"]/ul/li')
        for one in ids:
            one = 'seen_snote_ids[]=' + one.xpath('@data-note-id')[0]
            self.params.append(one)
        item = {}
        flag = 0
        read = re.findall(r'ic-list-read"></i> (\d+)', html)
        comment = re.findall(r'ic-list-comments"></i> (\d+)', html)
        result = response.xpath('//*[@id="list-container"]/ul/li/div')
        for one in result:
            item[1] = one.xpath('a/text()')[0]
            item[2] = one.xpath('div[1]/div/a/text()')[0]
            item[3] = one.xpath('div[1]/div/span/@data-shared-at')[0]
            item[4] = read[flag]
            try:
                item[5] = comment[flag]
            except:
                item[5] = u''
            item[6] = one.xpath('div[2]/span/text()')[0].strip()
            try:
                item[7] = one.xpath('div[2]/span[2]/text()')[0].strip()
            except:
                item[7] = u'0'
            try:
                item[8] = one.xpath('div[2]/a[1]/text()')[0]
            except:
                item[8] = u''
            flag += 1
            row = [item[i] for i in range(1, 9)]
            self.write.writeRow(row)


if __name__ == "__main__":
    jian = Spider()
    jian.totalPage()
