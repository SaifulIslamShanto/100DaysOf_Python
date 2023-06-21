num = int(input('Enter a Number Here : '))

if num < 0:
    print("Please Enter Positive Number")
else:
    sum = 0
    while num > 0:
        sum += num
        num -= 1
    print(sum)
