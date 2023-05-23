# Raising custom errors in Python | Python Tutorial - Day #38
# https://replit.com/@codewithharry/38-Day38-Custom-Errors#main.py
# -> https://docs.python.org/3/library/exceptions.html

"""
    * raise  ব্যবহার করে Custom Error Show করানো যায় এবং প্রোগ্রাম থামিয়ে দেওয়া হয়।
"""

""" num = int(input("Enter any valye between 5 to 9 : "))

if (num < 5 or num > 9):
    raise ValueError("Value Should be between 5 to 9")

print("Your Enter Value is : ", num); """


"""

Enter any valye between 5 to 9 : 10
Traceback (most recent call last):
  File "f:\Programming\Python\03_Practice\100DaysOfCode-Python\Learning\30_RaisingCustomError.py", line 11, in <module>
    raise ValueError("Value Should be between 5 to 9")
ValueError: Value Should be between 5 to 9

"""


""" num = input("Enter any valye between 5 to 9 : ")


if (num == 'quit'):
    print("program is quit")
elif (int(num) < 5 or int(num) > 9):
    raise ValueError("Value Should be between 5 to 9")

print("Your Enter Value is : ", num) """


num = input("Enter any valye between 5 to 9 : ")

looping = True
while looping:
    try:
        if (num == 'quit'):
            print("program is quit")
            break
        elif (int(num) < 5 or int(num) > 9):
            raise ValueError("Value Should be between 5 to 9")
        # else:
        #     looping = False
        print("Your Enter Value is : ", num)
    except IndexError:
        print("You Type String Value")
