# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

import pymysql


def create_table():
    db = pymysql.connect('localhost', 'root', '1234', 'db_py_basic')
    cursor = db.cursor()
    cursor.execute('drop table if exists employee')
    sql = """create table employee (
        first_name char(20) not null,         
        last_name char(20),
        age int,
        sex char(1),
        income float,
        create_time datetime
    )"""
    try:
        cursor.execute(sql)
        print('create table success')
    except Exception as e:
        print('create table failed, case: %s' % e)
    finally:
        db.cursor()


def main():
    create_table()


if __name__ == '__main__':
    main()
