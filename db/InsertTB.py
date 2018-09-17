# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

import pymysql
import datetime


def insert_record():
    db = pymysql.connect('localhost', 'root', '1234', 'db_py_basic')
    cursor = db.cursor()
    sql = "insert into employee(first_name, last_name, age, sex, income,create_time)" \
          "values('%s', '%s', %d, '%c', %d, '%s')" \
          % ('xiao', 'zhi', 22, 'M', 12345, datetime.datetime.now())
    try:
        cursor.execute(sql)
        db.commit()
        print('insert success')
    except Exception as e:
        print('insert failed case:%s' % e)
        db.rollback()
    finally:
        db.close()


def main():
    insert_record()


if __name__ == '__main__':
    main()
