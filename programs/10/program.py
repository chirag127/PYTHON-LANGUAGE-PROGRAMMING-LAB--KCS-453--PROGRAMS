# To write a python program selection sort.


def selection_sort(list):
    for i in range(len(list) - 1):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return list


print(selection_sort([1, 2, 3, 15, 5, 6, 7, 8, 9, 10]))
