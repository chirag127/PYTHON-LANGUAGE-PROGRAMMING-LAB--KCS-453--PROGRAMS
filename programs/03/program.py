def gcd(a, b):
    return b if a == 0 else gcd(b % a, a)


a = int(input("Enter 1st no: "))
b = int(input("Enter 2nd no: "))
print("The GCD of", a, "and", b, "is", gcd(a, b))
import math

print("The GCD of", a, "and", b, "is", math.gcd(a, b))
