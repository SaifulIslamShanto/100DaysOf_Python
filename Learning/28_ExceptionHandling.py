# Exception Handling in Python | Python Tutorial - Day #36

""" 
* একটি প্রগ্রাম এ যদি কোন error আসে সেইটা স্কিপ করে অন্য প্রোগ্রাম গুলো যেনো রান করে সেইটা দেকবো try & Except দিয়ে 

"""
""" a = input("Enter the Number : ")
print(f"Multiplicatin Table of {a} is :")

try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("Invalid Input!")

print("Other Program of code")
print("End of program") """

# -> Multiple ERROR Handaling

try:
    num = int(input("Enter An Integer: "))
    # a = [6, 3]
    # print(a[num])
except ValueError:
    print("Number Entered in not and Integer.")

except IndexError:
    print("IndEX Error")


# /https://www.tutorialsteacher.com/python/error-types-in-python
# https://www.programiz.com/python-programming/exception-handling
