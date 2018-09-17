# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

class MyClass(object):
    i = 123

    def __init__(self, name):
        self.__name = name

    def get__name(self):
        return self.__name

    def set__name(self, name):
        self.__name = name

    def __str__(self) -> str:
        return '%s' % self.__name

    __repr__ = __str__

    def func(self):
        return 'success' + self.get__name()


if __name__ == '__main__':
    use_calss = MyClass('name')
    print(use_calss.i)
    print(use_calss.func())
    use_calss.set__name('rename')
    print(use_calss.get__name())
    print(use_calss)
