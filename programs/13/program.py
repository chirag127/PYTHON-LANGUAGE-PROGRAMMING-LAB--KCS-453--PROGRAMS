import re


def isPrime(n):
    return re.match(r"^1?$|^(11+?)\1+$", "1" * n) is None


N = int(input("Enter a number: "))
M = 100
l = []
while len(l) < N:
    l += filter(isPrime, range(M - 100, M))
    M += 100
print(l[:N])
