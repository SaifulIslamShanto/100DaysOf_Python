# Find the Largest Among Three Numbers

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
num3 = int(input("Enter Third Number : "))

if (num1 > num2 and num1 > num3):
    print(num1, " Is Largest Number")
elif (num2 > num1 and num2 > num3):
    print(num2, " Is Largest Number")
else:
    print(num3, " Is Largest Number")
