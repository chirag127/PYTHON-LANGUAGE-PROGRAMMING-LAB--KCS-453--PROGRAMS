# To write a python program linear search.

def linear_search(arr, x):
    found = False
    pos = 0
    while pos < len(arr) and not found:
        if arr[pos] == x:
            found = True
        else:
            pos += 1


    return found, pos

print(linear_search([1, 2, 3, 4, 5], 5))

