# Enumerate Function in Python | Python Tutorial - Day #42
""" 
    -> enumerate() ফাংশন ব্যবহার করে আমরা খুব সহজেই (list, Tupple, String) এর ইনডেক্স কাউন্ট করতে পারি। 


"""

""" 
marks = [12, 56, 32, 98, 12, 45, 1, 4]


for index, mark in enumerate(marks):
    print(marks)
    if (index == 3):
        print("Shanto, Is Awesome!")

 """


""" fruits = ["Apple", "Banana", "Mango", "Lichi", "Gowava", "Orange"]
for x, fruits in enumerate(fruits):
    print(x,fruits)
    if (x == 3):
        print("This Is Lichi")
 """

#  => Change The Start Index with 0 to 1

""" fruits = ["Apple", "Banana", "Mango", "Lichi", "Gowava", "Orange"]
for x, fruits in enumerate(fruits, start=1):
    print(x, fruits)
    if (x == 4):
        print(" => This Is Lichi") """


""" fruits = ["Apple", "Banana", "Mango", "Lichi", "Gowava", "Orange"]
for x, fruits in enumerate(fruits, start=1):
    print(f"{x} : {fruits}")
 """

# -> Tuple
""" colors = ("red", "Blue", "Green")

for indxe, colors in enumerate(colors):
    print(indxe, colors) """


# -> String

str = "HellowOrld"

for index, str in enumerate(str, start=1):
    # print(index, str)
    print(f"{index} : {str}")
