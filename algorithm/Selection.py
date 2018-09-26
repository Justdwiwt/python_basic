# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

def select_sort(arr):
    n = len(arr)
    for i in range(0, n):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]
    print(arr)


if __name__ == '__main__':
    a = [1, 3, -1, 32, -32, 43, 5, 0, 9, -3]
    select_sort(a)
