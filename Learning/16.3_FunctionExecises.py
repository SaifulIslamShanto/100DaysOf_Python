# Python functions - Exercises, Practice, Solution

# * 1. Write a Python function to find the maximum of three numbers.

""" def maxInTreeNumber():
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    c = int(input("Enter C Number : "))

    if (a > b and a > c):
        print(f"{a} A is Bigger Then B {b} and C {c}")
    elif (b > a and b > c):
        print(f"{b} B is Bigger Then A {a} and C {c}")
    elif (c > a and c > b):
        print(f"{c} C is Bigger Then A {a} and B {b}")
    else:
        print("Wrong Input")


print(maxInTreeNumber()) """

# * এখানে প্রথেমে maxOfTwo এর মধ্যে ২ সংখার মধ্যে maximum বের করবে 
def maxOfTwo(x, y):
    if x > y:
        return x
    else:
        return y


# * এখানে maxOfThree এর মধ্যে ২ সংখার মধ্যে maximum বের করবে 
def maxOfThree(x, y, z):
    return maxOfTwo(x, maxOfTwo(y, z))


print(maxOfThree(3, 6, -5))
