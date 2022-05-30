# Write a program to check that a given year is Leap Year or not.

n = int(input("Enter the year: "))

if n % 4 == 0:
    if n % 100 == 0 and n % 400 == 0 or n % 100 != 0:
        print("The year is a leap year")
    else:
        print("The year is not a leap year")
