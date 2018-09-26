# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

def shell_sort(arr):
    n = len(arr)
    gap = round(n / 2)
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j = j - gap
            arr[j] = temp
        gap = round(gap / 2)
    print(arr)


if __name__ == '__main__':
    lt = [1, 3, -1, 32, -32, 43, 5, 0, 9, -3]
    shell_sort(lt)
