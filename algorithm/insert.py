# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

def insert_sort(I):
    for i in range(len(I)):
        min_index = i
        for j in range(i + 1, len(I)):
            if I[min_index] > I[j]:
                min_index = j
        tmp = I[i]
        I[i] = I[min_index]
        I[min_index] = tmp
        print(str(I))
    print("result: " + str(I))


if __name__ == '__main__':
    lt = [1, 3, -1, 32, -32, 43, 5, 0, 9, -3]
    insert_sort(lt)
