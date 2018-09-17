# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

def quick_sort(L):
    qsort(L, 0, len(L) - 1)


def qsort(L, first, last):
    if first < last:
        split = partition(L, first, last)
        qsort(L, first, split - 1)
        qsort(L, split + 1, last)


def partition(L, first, last):
    # 选取列表中的第一个元素作为划分元素
    pivot = L[first]
    leftMark = first + 1
    rightMark = last
    while True:
        while L[leftMark] <= pivot:
            # 如果列表中存在与划分元素pivot相等的元素，让它位于left部分
            # 以下检测用于划分元素pivot是列表中的最大元素时
            # 防止leftMark越界
            if leftMark == rightMark:
                break
            leftMark += 1
        while L[rightMark] > pivot:
            # 这里不需要检测，划分元素pivot是列表中的最小元素时
            # rightMark自动停在first处
            rightMark -= 1
            if leftMark < rightMark:
                # 此时leftMark处的元素大于pivot
                # rightMark处的元素小于等于pivot，交换两者
                L[leftMark], L[rightMark] = L[rightMark], L[leftMark]
            else:
                break
            # 交换first处的划分元素与rightMark处的元素
            L[first], L[rightMark] = L[rightMark], L[first]
        # 返回划分元素pivot的最终位置
        return rightMark


# 函数调用示例
if __name__ == '__main__':
    num_list = [1, 3, -1, 32, -32, 43, 5, 0, 9, -3]
    print("排序前：" + str(num_list))
    quick_sort(num_list)
    print("排序后：" + str(num_list))
