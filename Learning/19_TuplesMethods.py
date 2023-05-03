""" countries = ("Bangladesh", "India", "USA", "UK", "England", "Gurmany")
print(countries)

# -> Change Tuples Value
temp = list(countries)      # -> First Convert Tuople TO LIST
temp.append("Russia")       # -> Add Item
temp.pop(3)                 # -> Remove Item
temp[2] = "Finland"         # -> Change Item
countries = tuple(temp)     # -> Convert Tuples
print(countries) """

# ('Bangladesh', 'India', 'Finland', 'England', 'Gurmany', 'Russia')

# -> Concatinate Tuples

""" countries = ("Bangladesh",)
# countries = ("Bangladesh", "india")
print(countries)
Cites = ("Dhaka", "Naraygonj", "Mirpur")
countriesWithCitys = countries + Cites
print(countriesWithCitys) """


# -> count(methods)
""" tuple1 = (0, 1, 2, 3, 5, 4, 3, 2, 3, 2)
countTuple = tuple1.count(3)
print("Count of 3 in Tuples Is : ", countTuple) """

# -> index(methods)
tuple1 = (0, 1, 2, 3, 5, 4, 3, 2, 3, 2)
# countTuple = tuple1.index(2)

countTuple = tuple1.index(3, 5, 9)
# countTuple = tuple1.index(Element,Start,end)
print("index of 3 in Tuples Is : ", countTuple)
