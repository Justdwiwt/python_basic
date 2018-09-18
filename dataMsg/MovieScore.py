# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

from common.mysql_client import *
from common.csv_utils import *
from common.email_server import *

score_range_csv = 'D:\score_range.csv'


def movie_score_range():
    query_sql = "select movieName,showYear,makeCounty,movieType,movieScore " \
                "from douban_comment order by movieScore desc "
    query_result = query_table(query_sql)
    return query_result


def write_into_csv():
    head = ['电影名称', '上映年份', '制作国家', '电影类别', '电影评分']
    score_range_record = movie_score_range()
    out_put_data = []
    for row in score_range_record:
        out_put_data.append(row)
        write_csv_file(score_range_csv, head, out_put_data)


def main():
    write_into_csv()
    to = ['email@aliyun.com']
    cc = ['email@aliyun.com']
    subject = '评分排行榜'
    content = '评分排行榜数据'
    send(to, cc, subject, content, [score_range_csv], True)


if __name__ == '__main__':
    main()
