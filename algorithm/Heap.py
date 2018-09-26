# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

def heap_sort(arr):
    n = len(arr)
    first = int(n / 2 - 1)
    for start in range(first, -1, -1):
        max_heapify(arr, start, n - 1)
    for end in range(n - 1, 0, -1):
        arr[end], arr[0] = arr[0], arr[end]
        max_heapify(arr, 0, end - 1)
    print(arr)
    return arr


def max_heapify(arr, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            break


if __name__ == '__main__':
    lt = [1, 3, -1, 32, -32, 43, 5, 0, 9, -3]
    # noinspection PyTypeChecker
    heap_sort(lt)
