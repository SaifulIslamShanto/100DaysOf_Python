""" dic = {
    # -> "keys" : "Values"
    "Shanto": "Learn Programming",
    "Programming": "python",
    1: "c Programming",
    2: "c++ Programming",
    3: "python Programming"
}
# -> Access Dictonary
print(dic)
# -> # -> Access indivusual Dictonary item keys
# * if they didn't find item keys its show "Error"
print(dic["Shanto"])
print(dic[3])
# -> # -> Access indivusual Dictonary item keys
# * if they didn't find item keys its show "none"
print(dic.get(2)) """

# => 2

""" info = {
    "Name": "Saiful Islam Shanto",
    "Hobby": "Programmming",
    "Number": 1710561898,
    "LoveProgrammanig?": True
}

print(info)
print(info.keys())
print(info.values()) """

""" for key in info.keys():
    print(info[key]) """

""" for key in info.keys():
    print(f"The Value Corresponding to the key {key} is {info[key]}") """


# => 3

info = {
    "Name": "Saiful Islam Shanto",
    "Hobby": "Programmming",
    "Number": 1710561898,
    "LoveProgrammanig?": True
}

print(info.items())

for key, value in info.items():
    print(f"The Value Corresponding to the key {key} is {value}")


# https://replit.com/@codewithharry/33-Day-33-Dictionary#main.py
# https://www.programiz.com/python-programming/dictionary