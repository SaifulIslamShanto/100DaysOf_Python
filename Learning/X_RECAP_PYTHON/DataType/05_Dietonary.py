""" my_dictionary = {}
myMarks = {"Bengali": 80, "English": 95, "Math": 50}

# print(my_dictionary)
print(myMarks["Math"]) """

""" my_marks = {
    "Bengali": [30, 35, 32],
    "English": [45, 52, 33],
    "Math": [60, 74, 58]
}
print(my_marks["Math"]) """

""" my_marks = {True: "Bengali"}
print(my_marks)
 """

#  *---------

a = {'name': 'Shanto', 'number': '01111'}
print(a)
print(a['name'])

a['name'] = 'Saiful'
print("Name After Change : ", a['name'])
print(a['number'])

del a['number']
# print("Number After Delete : ", a['number'])
print(a)

a.clear()
print(a)
