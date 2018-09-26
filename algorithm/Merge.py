# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = int(len(arr) / 2)
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


def merge(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    print(result)
    return result


if __name__ == '__main__':
    lt = [1, 3, -1, 32, -32, 43, 5, 0, 9, -3]
    # noinspection PyTypeChecker
    merge_sort(lt)
