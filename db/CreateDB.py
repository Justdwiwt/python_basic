# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

import pymysql


def db_connect():
    db = pymysql.connect('localhost', 'root', '1234', 'my_test_sql')
    cursor = db.cursor()
    cursor.execute('select version()')
    data = cursor.fetchone()
    print('Database version:%s' % data)
    db.close()


def main():
    db_connect()


if __name__ == '__main__':
    main()
