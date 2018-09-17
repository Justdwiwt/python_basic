# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

import pymysql


def delete_record():
    db = pymysql.connect('localhost', 'root', '1234', 'db_py_basic')
    cursor = db.cursor()
    sql = "delete from employee where age > %d" % 22
    try:
        cursor.execute(sql)
        db.commit()
        print('delete success')
    except Exception as e:
        print('Delete record failed. Case: %s' % e)
        db.rollback()
    finally:
        db.close()


def main():
    delete_record()


if __name__ == '__main__':
    main()
