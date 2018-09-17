# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

L = [1, 2]
L.append(L)
print(L)


# x = -2
# assert x > 0, 'ss'

# i = 0
# while i <= 10:
#     L.append(i)
#     i += 1
# print(L)

def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact(5))


def fun_sum(x, y):
    return x + y


var = lambda x, y: x + y
print(var(2, 3))


def fun_join(x):
    return x > 3


f_list = filter(fun_join, [1, 22, 5, 2, 0])

print([item for item in f_list])
print([item for item in filter(lambda x: x > 3, [1, 22, 5, 2, 0])])
