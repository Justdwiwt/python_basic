# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

import pymysql


def update_table():
    db = pymysql.connect('localhost', 'root', '1234', 'db_py_basic')
    cursor = db.cursor()
    sql = "update employee set age=age+1 where sex='%s'" % 'M'
    try:
        cursor.execute(sql)
        db.commit()
        print('update success')
    except Exception as e:
        print('update table failed. Case: %s' % e)
        db.rollback()
    finally:
        db.close()


def main():
    update_table()


if __name__ == '__main__':
    main()
