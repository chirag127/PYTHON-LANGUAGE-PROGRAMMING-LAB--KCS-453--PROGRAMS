def power(x, y):
    return 1 if y == 0 else x * power(x, y - 1)


b = int(input("Enter the base: "))
e = int(input("Enter the exponent: "))
print("result: ", power(b, e))
