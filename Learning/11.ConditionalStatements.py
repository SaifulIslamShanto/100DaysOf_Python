# -> if , if else, if-else-elif , nested if-else-elif

# -> "Indentation" refers to the spaces at the beginning of a code line. | Indentation হচ্ছে কোড শুরু করার পূর্বে একটি স্পেস দিয়ে নেওয়াকে বুজায়।

"""
a = int(input("Enter your age : "))
print("Your age is : ", a)

if (a >= 18):
    print("You can Drive")
else:
    print("you can't drive")
"""
""" applePrice = 210
budget = 200
 
if(applePrice<=budget):
    print("add 1kg apples to the cart")
else:
    print("Don't add 1kg apples to the cart") """


# -> if / elif / else

""" num = int(input("ENter a value : "))

if (num < 0):
    print("Number is Negative.")
elif (num == 0):
    print("Number is Zero")
elif (num == 999):
    print("Number is Tripple9")
else:
    print("Number is Positive") """


# -> NESTED IF

num = int(input("Enter a Number : "))
if (num < 0):
    print("Number is Negative")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    elif (num > 20 and num <= 30):
        print("Number is between 20-30")
    else:
        print("Number is greater then 20")
else:
    print("Number is ZERO")
