# To write a python program to compute the GCD of two
# numbers.


def compute_gcd(a, b):
    return b if a == 0 else compute_gcd(b % a, a)

a = int(input("Enter the first number: "))

b = int(input("Enter the second number: "))

print("The GCD of", a, "and", b, "is", compute_gcd(a, b))

import math

print("The GCD of", a, "and", b, "is", math.gcd(a, b))