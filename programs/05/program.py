def newton_sqrt(n, num_iter=500):
    x = n / 2
    for _ in range(num_iter):
        x = x - ((x**2 - n) / (2 * x))
    return x


print(newton_sqrt(2))
import math

print(math.sqrt(2))
