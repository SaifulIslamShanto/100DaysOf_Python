checkYear = int(input("Enter A Year : "))

if (checkYear % 400 == 0) and (checkYear % 100 == 0):
    print(checkYear," Is Leap Year")
elif (checkYear % 4 == 0) and (checkYear % 100 != 0):
    print(checkYear," Is Leap Year")
else:
    print(checkYear," Is Not A leap Year")
