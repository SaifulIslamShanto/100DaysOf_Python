# Day 20
# -> Function

# def calculateGmean(a, b):
#     mean = (a*b)/(a+b)
#     print(mean)

# # -> Check Grater number


# def isGrater(a, b):
#     if (a > b):
#         print("A is Graeter")
#     else:
#         print("B Is Grater")

# def isLesser(a,b):
#     pass
# #-> We can write Function body Code Letter

# a = 9
# b = 80
# isGrater(a, b)
# calculateGmean(a, b)
# gmean = (a*b)/(a+b)
# print(gmean)

# -> CheckLeapYaer


""" def check_year(a):

    if ((a % 400) == 0):
        print(a, " Is a Leap Year")
    elif ((a % 100) == 0):
        print(a, " Is a NOT Leap Year")
    elif ((a % 4) == 0):
        print(a, " Is a Leap Year")
    else:
        print(a, " Is a NOT Leap Year")


check_year(int(input("Enter The year : "))) """


""" num1 = int(input("Enter A Number : "))
rem1 = num1 % 2

if (rem1 == 0):
    print(num1, "Is an Even Number")
else:
    print(num1, "Is an odd Number") """


# -> Check Even or oDd

def evenOrOdd(a):
    rem1 = a % 2
    if (rem1 == 0):
        print(a, "Is an Even Number")
    else:
        print(a, "Is an odd Number")


evenOrOdd(int(input("Enter a Number: ")))
