# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

def quick(L):
    quick_sort(L, 0, len(L) - 1)


def quick_sort(L, low, hight):
    i = low
    j = hight
    if i >= j:
        return L
    key = L[i]
    while i < j:
        while i < j and L[j] >= key:
            j -= 1
        L[i] = L[j]
        while i < j and L[i] <= key:
            i += 1
        L[j] = L[i]
    L[i] = key
    quick_sort(L, low, i - 1)
    quick_sort(L, j + 1, hight)
    return L


if __name__ == '__main__':
    a = [1, 3, -1, 32, -32, 43, 5, 0, 9, -3]
    quick(a)
    print(a)
