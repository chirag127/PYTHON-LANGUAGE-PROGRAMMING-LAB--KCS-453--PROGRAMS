# To write a python program Binary search.


def binary_search(list, item):
    first = 0
    last = len(list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if list[midpoint] == item:
            found = True
        elif item < list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return found


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))
