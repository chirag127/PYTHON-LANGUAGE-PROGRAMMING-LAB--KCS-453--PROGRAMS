# To write a python program find the maximum of a list of
# numbers.

n = int(input("Enter the number of elements in the list: "))

a = [int(input("Enter the number: ")) for _ in range(n)]

a.sort()

a.reverse()

print("The maximum number is: ", a[0])