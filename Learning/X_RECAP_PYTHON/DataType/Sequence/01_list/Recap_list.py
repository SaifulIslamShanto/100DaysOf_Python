# -> Diclear List

""" number = [1, 2, 3, 4, 5]
print(number) """

# * empty list
# myList = []


# * list with mixed data types
""" myList = [1, "Hello", 3.4]
print(myList) """


# * Access Python List Elements
""" languages = ["Python", "Swift", "C++"]
print(languages[0])
print(languages[1])
print(languages[2]) """

# * Negative Indexing in Python
""" languages = ["Python -3", "Swift -2", "C++ -1"]
print(languages[-1])
print(languages[-2])
print(languages[-3]) """

# * Slicing of a Python List
""" 
myList = ['S', 'H', 'A', 'N', 'T', 'O']

print(myList[2:5])  # * A','N','T' ->  index 2 to index 4
print(myList[:5])  # *'S','H','A','N','T' -> index 5 to the end
print(myList[:])  # *'S','H','A','N','T','0' -> returns all list items
 """


# -> Use Built In Function FOR LIST


""" 
    * append() ✅ 
    * extend() ✅ 
    * insert() ✅ 
    * remove() ✅ 
    * pop()
    * clear()
    * index()
    * count()
    * sort()
    * reverse()
    * copy()

"""


# * append()
""" numbers = [21, 35, 54, 12]
print("Before Append:", numbers)

# using append method
numbers.append(32)
print("After Append: ", numbers)
 """

# * extend()
# -> We use the extend() method to add all items of one list to another

""" prime_number = [2, 3, 5]
print('List_1', prime_number)
Even_number = [4, 6, 8]
print('List_2', Even_number)

# join two lists
prime_number.extend(Even_number)
print("List after extend 2 List:", sorted(prime_number)) """

# *Change List Items
""" numbers = [21, 35, 54, 12]
print("Before AddED Number :", numbers)
numbers[2] = 100
print("After AddED Number :", numbers) """

# -> Remove an Item From a List

# * 1. Using del()
""" numbers = [21, 35, 54, 12]
# del numbers[1] #[21, 54, 12]
del numbers[-1] #[21, 35, 54]
print(numbers) """


# * 2. Using remove()
""" numbers = [21, 35, 54, 12]
numbers.remove(35)
print(numbers) """


# * insert()
""" vowel = ['a', 'e', 'i', 'u']
# 'o' is inserted at index 3 (4th position)
# -> Index , addITEM
vowel.insert(3, 'o')
print(vowel) """


# * pop()
""" vowel = ['a', 'e', 'i', 'u']
vowel.pop(3) # ['a', 'e', 'i']
print(vowel) """


# * clear()  #< removes all items from the list
""" vowel = ['a', 'e', 'i', 'u']
vowel.clear()  # ['a', 'e', 'i']
print(vowel) """

# * index() -> Check INDEX Of list ITEM
""" vowel = ['a', 'e', 'i', 'u']
x = vowel.index('e')
print(x) """

# * count()
""" vowel = ['a', 'e', 'i', 'u', 'e', 'a', 'e', 'a']
x = vowel.count('a')
print(x) """


# * sort()
""" vowel = [1, 4, 5, 7, 1, 32, 5, 4, 4, 3]
vowel.sort()
print(vowel) """


# * reverse()
""" vowel = [1, 4, 5, 7, 1, 32, 5, 4, 4, 3]
vowel.reverse()
print(vowel) """

# * copy() ()
""" vowel = [1, 4, 5, 7, 1, 32, 5, 4, 4, 3]
nmbers = vowel.copy()
print(nmbers) """

# -------------------------------------------------------

# * Iterating through a List
""" language = ['python', 'swift', 'c++']
for i in language:
    print(i) """

# * Check if an Item Exists in the Python List
""" language = ['python', 'swift', 'c++']
print('c' in language)
print('python' in language) """

# * Python List Length
""" language = ['python', 'swift', 'c++']
print(len(language)) """

# Python List Comprehension -> NEED TO LEARN

numbers = [number*number for number in range(1, 6)]
print(numbers)
