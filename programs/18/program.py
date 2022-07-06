# Write a Python program to print ‘n terms of Fibonacci series using iteration.

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        print(a, end=' ')
    print()

fibonacci(10)