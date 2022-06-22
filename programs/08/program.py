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

# make above function shorter
def linear_list_search(arr, x):
    return x in arr, arr.index(x)


print(linear_list_search([1, 2, 3, 4, 5], 5))
