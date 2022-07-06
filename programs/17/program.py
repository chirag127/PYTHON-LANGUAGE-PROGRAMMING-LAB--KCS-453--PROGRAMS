# Write a program to check that a given year is Leap Year or not.

n = int(input("Enter the year: "))
if (n % 4 == 0) and (n % 100 != 0) or (n % 400 == 0):
    print("The year is a leap year.")
