""" marks = [3, 5, 6 , "Shanto", True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4]) """

# -> list INDEX

""" colors = ["RED", "Green", "Blue", "Yellow", "Pink"]
print(colors[0])
print(colors[1])
print(colors[2])
print(colors[3])
print(colors[4]) """


# -> list Negative INDEXING

""" colors = ["RED", "Green", "Blue", "Yellow", "Pink"]
print(colors[-3]) # -> Negative Index
print(colors[len(colors)-3]) # -> Positive Index
print(colors[5-3]) # -> Positive Index
print(colors[2]) # -> Positive Index """


# -> Check Whether and item in present in the list
""" colors = ["RED", "Green", "Blue", "Yellow", "Pink"]
if "Yellow" in colors:
    print("Yellow is Present.")
else:
    print("Yellow Is Absent") """


# -> Print elements within a particuler range
""" colors = ["RED", "Green", "Blue", "Yellow", "Pink"]
print(colors)
print(colors[:])
# print(colors[1:4:Jump Index ])
print(colors[1:5:2]) """


# -> List Comprehension
""" 

lst = [i*i for i in range(4)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)

"""

names = ["Milo", "Sarah", "Bruno", "Abastasia", "Rose"]
namesWith_o = [item for item in names if "o" in item]
print(namesWith_o)
