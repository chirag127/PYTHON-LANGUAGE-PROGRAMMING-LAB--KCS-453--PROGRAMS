# To write a python program Insertion sort.

def insertion_sort(list):
    for i in range(1, len(list)):
        j = i
        while j > 0 and list[j] < list[j - 1]:
            list[j], list[j - 1] = list[j - 1], list[j]
            j -= 1
    return list

print(insertion_sort([1, 2, 3, 15, 5, 6, 7, 8, 9, 10]))