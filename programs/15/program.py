# Write a Python program to compute area and circumference of a
# triangle. Take input from user.

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))


def area_of_triangle(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

def circumference_of_triangle(a, b, c):
    return a + b + c

print("Area of the triangle is: ", area_of_triangle(a, b, c))
print("Circumference of the triangle is: ", circumference_of_triangle(a, b, c))
