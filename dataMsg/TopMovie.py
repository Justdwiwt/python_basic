# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

from common.mysql_client import *
from common.csv_utils import *
from common.email_server import *

top10_make_county_csv = 'D:\\top10_make_county.csv'


def make_county_top10():
    query_sql = "select makeCounty,count(1) " \
                "from douban_comment group by makeCounty " \
                "order by count(1) desc limit 10"
    query_result = query_table(query_sql)
    return query_result


def write_into_csv():
    head = ['制作国家', '制作电影数']
    score_range_record = make_county_top10()
    out_put_data = []
    for row in score_range_record:
        out_put_data.append(row)
        write_csv_file(top10_make_county_csv, head, out_put_data)


def main():
    write_into_csv()
    to = ['email@aliyun.com']
    cc = ['email@aliyun.com']
    subject = 'make county top 10'
    content = 'make county'
    send(to, cc, subject, content, [top10_make_county_csv], True)


if __name__ == '__main__':
    main()
