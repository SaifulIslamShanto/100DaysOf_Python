def evenOrOdd(num):
    rem1 = num % 2
    if (rem1 == 0):
        print(num, "Is an Even Number")
    else:
        print(num, "Is an odd Number")


evenOrOdd(int(input("Enter a Number: ")))
