# https://www.youtube.com/watch?v=Ca1NYpE3QWg&list=PLjVLYmrlmjGf3jtxG8lSo-zaPktQ7YbUw&index=15

import random

cNumber = random.randrange(1, 10)
userInput = int(input("Enter Your Number : "))

if userInput > cNumber:
    print("Computer Number : ", cNumber)
    print("Your Guess Number is too High")
elif cNumber > userInput:
    print("Computer Number : ", cNumber)
    print("Your Guess Number is too Low")
else:
    print("Computer Number : ", cNumber)
    print("Your Guess Number is Equal")
