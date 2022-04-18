# To write a python program to perform Matrix Multiplication.

from unittest import result


A = []

n = int(input("Enter the N for N x N matrix: "))

print("Enter the elements of the matrix: ")

for i in range(n):
    A.append([])
    for _ in range(n):
        A[i].append(int(input()))

print("The matrix is: ")
print(A)

# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Display the 2D array

print("Display Array In Matrix Format: ")

for i in range(n):
    for j in range(n):
        print(A[i][j], end=" ")
    print()

B = []

n = int(input("Enter the N for N x N matrix: "))

# use list for storing the matrix

# get the user input and store it in the list ( here INPUT is taken from the user i.e. 1 2 3 4 5 6 7 8 9)

print("Enter the elements of the matrix: ")

for i in range(n):
    B.append([])
    for _ in range(n):
        B[i].append(int(input()))


print("The matrix B is: ")

print(B)

# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Display the 2D array

print("Display Array In Matrix Format: ")

for i in range(n):
    for j in range(n):
        print(B[i][j], end=" ")
    print()

result = []

# multiply A and B and store the result in result

for i in range(len(A)):
    result.append([])
    for j in range(len(B[0])):
        result[i].append(0)
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

print("The result of the multiplication is: ")

for r in result:
    print(r)

