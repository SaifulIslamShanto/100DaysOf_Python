
# -> add 2 number :- pre-fedined Variables
""" num1 = 10
num2 = 20
addTwoNumber = num1+num2
print("The Number is : ", addTwoNumber) """

# -> add 2 number from userInput
""" num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
addTwoNumber = num1+num2
print("The Number is : ", addTwoNumber)
 """
 
# -> add 2 number from userInput using function


def addTwoNumber():
    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter Second Number : "))
    return num1+num2


print(addTwoNumber())
