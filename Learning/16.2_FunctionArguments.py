# Video Day 21

"""
    -> Note
    => function arguments and return statement
        * Default Arguments
        * Keyword Arguments
        * Variable Length Arguments
        * Requrid Arguments 

"""

""" 
# -> Defalut Arguments
# * -> এখানে ভেলু ফাংশনে ডিক্লিয়ার করা থেকে আগে থেকে এবং প্রয়োজন এ ফাংশন কল করার সময় ভেলু চেঞ্জ করা যায়।
def average(a=9, b=1):
    print("The Average is ", (a+b)/2)


average(10, 6)
average()
average(10)
average(b=10)
 """

# def name(firstName, middleName="jhon", lastName="Whatson"):

""" 
def name(firstName="Saiful", middleName="Islam", lastName="shanto"):
    # def name(firstName, middleName, lastName):
    print("Hello", firstName, middleName, lastName)


name("shanto","Web","Devloper")
 """


# * Keyword Arguments

""" def avg(a=1,b=2):
    print("The Average is ", (a+b)/2)

avg(b=5, a=10) """


""" # * Requried Agrumnets
# -> ফাংশন এ যদি Agrumnets নেওয়া হয় এবং সেইটার ভেলু ডিক্লিয়ার করা না হয় তাহলে ফাংশন ডিক্লিয়ার এর সময় সেইটার মান দিতে হবে এবং এটাই রিকয়ার্ড আর্গুমেন্ট।

def sum(a, b, c=10):
    print("Total Sum is : ", (a+b+c))

sum(10, 5)
# Total Sum is :  25 """


# * -> Variable Length Arguments

""" def avg(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum+i
    print("Avg is : ", sum/len(numbers))


avg(5, 6,1) """

""" 
def name(**name):
    print(type(name))
    print("Hello,",
          name["fname"],
          name["mname"],
          name["lname"]
          )


name(
    mname="Buchanan",
    lname="Barnes",
    fname="James"
)
 """

# * return Statement


""" def avg(*numbers):
    sum = 0
    for i in numbers:
        sum = sum+i
    return sum / len(numbers)


c = avg(5, 6, 7, 1)
print(c) """


def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname


print(name("James", "Buchanan", "Barnes"))

# https://replit.com/@codewithharry/21-Day-21-Function-Arguments#.tutorial/Tutorial.md
