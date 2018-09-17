# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

import csv


def write_csv_file(path, head, data):
    try:
        with open(path, 'w', newline='')as csv_file:
            writer = csv.writer(csv_file, dialect='excel')
            if head is not None:
                writer.writerow(head)
            for row in data:
                writer.writerow(row)
                print('Write a CSV file to path %s Successful.' % path)
    except Exception as e:
        print('Write a CSV file to path: %s, Case: %s' % (path, e))
