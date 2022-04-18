# To write a python program find the square root of a number
# (Newton’s method).

def newton_sqrt(n,num_iter=500):
    x = n/2
    for _ in range(num_iter):
        x = x - ((x**2 - n)/(2*x))
    return x

print(newton_sqrt(2))