# Map, Filter and Reduce in Python | Python Tutorial - Day #53

# -> map()


# * Map() ফাংশন ব্যবহার করে (List,set,Tuple) এর মধ্যে প্রতিটি আইটেমের মধ্যে এক্সেস করে

# * map() কোনো  (List,set,Tuple) কল করলে সেটা সেই  (List,set,Tuple) প্রত্যেকটা আইটেমের উপর আপনারই দেওয়া একটা ফাংশন অ্যাপ্লাই করবে, এবং সবশেষে সবগুলো আবার আরেকটা অ্যারে হিসেবে রিটার্ন করবে

# * lambda Function  ও ব্যবহার করা যায়


""" def cube(x):
    return x*x*x

lists = [1, 2, 3, 4, 5, 8, 9]
newLists = list(map(cube, lists))
print(newLists) """

# -> Map With lambda Function

"""
lists = [1, 2, 3, 4, 5, 8, 9]
newLists = list(map(lambda x: x*x*x, lists))
print('Map Function Value : ', newLists) """

""" 
# def make_double(x):
#     return x*2


my_makrs = [10, 12, 20, 30]
# result = map(make_double, my_makrs)

# £using Lambda Function
result = map(lambda make_double: make_double*2, my_makrs)
# Result Conver in List
print(list(result)) """


# *------------------------------------------------

# -> filter()
# * ফিল্টার সেইম ম্যাপের মতোই কিন্তু এখানে অ্যাপ্লাইকৃত ফাংশন যদি true রিটার্ণ করে তাহলেই সেটা নতুন (List,set,Tuple) স্থান পাবে, নতুবা যদি ফাংশন false রিটার্ণ করে তাহলে সেই আইটেম অ্যারেতে স্থান পাবে না।

""" lists = [1, 2, 4, 6, 4, 3]


def filterFucntion(a):
    return a > 5


newLists = list(filter(filterFucntion, lists))
print('Filter Function : ', newLists) """

#  -> Filter() With Lambda Function

""" lists = [1, 2, 4, 6, 4, 3]


newLists = list(filter(lambda x: x > 2, lists))
print('Filter Function : ', newLists) """

# * is_even ফাংশনটি এর কাছে আসা ভ্যালু জোড় হলে True এবং নাহলে False রিটার্ন করে।


""" def is_even(x):
    return x % 2 == 0


numbers = [1, 2, 3, 4, 5, 6]
# resultForEven = filter(is_even, numbers)
resultForODD = filter(lambda is_Odd: is_Odd % 2 != 0, numbers)
print(list(resultForODD))
 """

# *------------------------------------------------


# List OF Numbers
""" from functools import reduce
numbers = [1, 2, 3, 4, 5]

# Calculate The Sum of number using Function / Lamda Function


def sum(x, y):
    return x+y


mySum = reduce(sum, numbers)

# Print The SUm
print(mySum) """


# -> Practice

# * Map();

""" def cube(x):
    return x*x*x """

""" number = [1, 2, 3, 4, 5, 6, 7, 8]
newNumber = list(map(lambda x: x*x*x, number))
print(newNumber) """


from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x+y, numbers)
print(sum_of_numbers)
