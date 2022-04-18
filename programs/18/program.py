#Write a Python program to print ‘n terms of Fibonacci series using iteration.

n = int(input("Enter the number of terms: "))

def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

fibonacci(n)