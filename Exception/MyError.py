# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

class MyError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return 'self define error'


def my_error_test():
    try:
        raise MyError()
    except MyError as e:
        print('exception info:', e)
    finally:
        print('passed')


if __name__ == '__main__':
    my_error_test()
