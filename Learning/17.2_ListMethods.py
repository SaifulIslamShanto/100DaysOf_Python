# ✌️
# -> List Methods

# *-< Append
""" listS = [1, 2, 3, 4, 5]
print(listS)
listS.append(7)  # -> For Add Value in list
print(listS)
listS.append("7")  # -> For Add Value in list
print(listS) """

# *-< sort()
""" 
listS = [11, 22, 3, 4, 5]
listS.sort()  # -> ছোট থেকে বড় আকারে আসবে
listS.sort(reverse=True)  # -> বড় থেকে ছোট আকারে আসবে
print(listS) """

# *-< Reverse()
"""
   listS = [11, 22, 3, 4, 5]
   listS.reverse()  # -> বড় থেকে ছোট আকারে আসবে
   print(listS) 
"""


# *-< index()
""" listS = [11, 22, 3, 4, 5]
print(listS.index(4))  # -> Find Index
print(listS) """

# *-< count()
""" listS = [11, 22, 3, 4, 5, 4]
print(listS.count(4))  # -> লিস্ট এর মধ্যে কতবার একটা ভেলু আছে সেইটা কাউন্ট করে।
print(listS) """

# *-< copy()
""" listS = [11, 22, 3, 4, 5, 4]
print(listS)
cpy = listS.copy()
cpy[0] = 0
print(cpy) """


# *-< insert()
# -> লিস্ট এ নতুন ভেলু এড করবে।
""" listS = [11, 22, 3, 4, 5, 4]
print(listS)
listS.insert(2, 99)
print(listS)
 """

# *-< max()
# -> finc max in list
""" listS = [11, 22, 3, 4, 5, 4]
print(listS)
print(max(listS)) """


# *-< extend()
# -> নতুন কোন লিস্ট আগের লিস্ট এর সাথে এড করা যায়।
""" listS = [11, 22, 3, 4, 5, 4]
print(listS)
m = [900, 1000, 1110]
listS.extend(m)
print(listS) """


listS = [11, 22, 3, 4, 5, 4]
print(listS)
m = [900, 1000, 1110]
extd = listS+m
print(extd)


""" 
 -> https://www.programiz.com/python-programming/methods/list
 -> https://www.w3schools.com/python/python_ref_list.asp
 -> https://docs.python.org/3/tutorial/datastructures.html
 
 -> https://www.datacamp.com/tutorial/python-list-function
"""
