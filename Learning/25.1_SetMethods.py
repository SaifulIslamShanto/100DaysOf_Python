# Set Methods

# -> Union
# -> union করার ফলে num1 এবং num2 এর ভেলু মিলে একটি সেট তেরি হবে।
""" num1 = {1, 2, 5, 6}
num2 = {3, 6, 7}
print(num1.union(num2)) """

# -> Update
# -> এখানে আপডেট করলে num1 এর সাথে num2 এর মান মিলে যাবে।
""" num1 = {1, 2, 5, 6} # {1, 2, 3, 5, 6, 7}
num2 = {3, 6, 7}
num1.update(num2) 
print(num1, num2) """

# -> Update & Union
""" cities1 = {"Dhaka", "Narayangonj", "Khulna", "Chandpur", "Gazipur"}
cities2 = {"Dhaka", "Dilli", "Kabul", "Tokyo"}

# unionCities = cities1.union(cities2)
cities1.update(cities2)
print(cities1, cities2) """


# ----------------------------------

#   -> Intersection
#   -> যে ভেলু টা ২ সাইডেই আছে সেইটাকে প্রিন্ট করবে
""" cities1 = {"Dhaka", "Narayangonj", "Khulna", "Chandpur", "Gazipur"}
cities2 = {"Dhaka", "Narayangonj", "Dilli", "Kabul", "Tokyo"}

# IntersectionCities = cities1.intersection(cities2)
# print(IntersectionCities)

cities1.intersection_update(cities2)
print(cities1) """

#   -> symmentric Difference
# -> যে ভেলুগুলো মিলে যাবে সেগুলো প্রিন্ট হবে না
""" cities1 = {"Dhaka", "Narayangonj", "Khulna", "Chandpur", "Gazipur"}
cities2 = {"Dhaka", "Narayangonj", "Dilli", "Kabul", "Tokyo"}

Cities = cities1.symmetric_difference(cities2)
print(Cities) """

# https://www.programiz.com/python-programming/set


# -> Remove()
""" num1 = {1, 2, 5, 6}
num2 = {3, 6, 7}
num1.remove(2)
print(num1) """

# -> discard()
""" num1 = {1, 2, 5, 6}
num2 = {3, 6, 7}
# num1.discard(2)
num1.discard(23)
print(num1) """

# -> pop()
""" num1 = {1, 2, 5, 6}
item = num1.pop()
print(num1)
print(item) """

# -> del()
num1 = {1, 2, 5, 6}
del num1
print(num1)
