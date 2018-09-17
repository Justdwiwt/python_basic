# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

def bubble(bubbleList):
    listLength = len(bubbleList)
    while listLength > 0:
        for i in range(listLength - 1):
            if bubbleList[i] > bubbleList[i + 1]:
                tmp = bubbleList[i]
                bubbleList[i] = bubbleList[i + 1]
                bubbleList[i + 1] = tmp
        listLength -= 1
        print(bubbleList)


if __name__ == '__main__':
    a = [1, 3, -1, 32, -32, 43, 5, 0, 9, -3]
    bubble(a)
