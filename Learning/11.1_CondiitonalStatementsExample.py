# Maximum

""" a = 10
b = 20
if (a > b):
    print(a, "A Is Maximum")
else:
    print(b, "B Is Maximum")
 """

#  -> Check Leap Year
# Write a C program to find whether a given year is a leap year or not.

""" check_year = int(input("Enter Year : "))
if ((check_year % 400) == 0):
    print(check_year, " Is a Leap Year")
elif ((check_year % 100) == 0):
    print(check_year, " Is a NOT Leap Year")
elif ((check_year % 4) == 0):
    print(check_year, " Is a Leap Year")
else:
    print(check_year, " Is a NOT Leap Year") """

# https://www.w3resource.com/c-programming-exercises/conditional-statement/index.php

# -> Even & ODD

""" num1 = int(input("Enter A Number : "))
rem1 = num1 % 2

if (rem1 == 0):
    print(num1, "Is an Even Number")
else:
    print(num1, "Is an odd Number") """


# -> Positive & Negative

num = int(input("Enter a Number : "))
if (num < 0):
    print(num, "Its Nagative Number ")
elif (num == 0):
    print(num, "Is ZERO")
else:
    print(num, "Its Positive")
