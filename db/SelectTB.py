# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

import pymysql


# noinspection PyUnboundLocalVariable,SpellCheckingInspection
def query_data():
    db = pymysql.connect('localhost', 'root', '1234', 'db_py_basic')
    cursor = db.cursor()
    sql = "select * from employee where income >%d" % 10000
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            create_time = row[5]
        print("first_name=%s,last_name=%s,age=%d,sex=%s,income=%d,create_time=%s" % (
            fname, lname, age, sex, income, create_time))
    except Exception as e:
        print('Error: unable to fecth data. Error info: %s' % e)
    finally:
        db.close()


def main():
    query_data()


if __name__ == '__main__':
    main()
