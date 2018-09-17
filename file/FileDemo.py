# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

if __name__ == '__main__':
    path = 'D:\\Python_Project\\Py_Basic_37\\file\\text.txt'
    rpath = '../file/text.txt'
    f_name = open(path, 'r')
    r_name = open(rpath, 'w')
    print('path:' + f_name.name)
    print('re_path:' + r_name.name)
    # print('r_path result(5):', r_name.read(5))
    r_name.write('9876543210')
    print('f_path result(all):', f_name.read())
    f_name.close()
    r_name.close()
