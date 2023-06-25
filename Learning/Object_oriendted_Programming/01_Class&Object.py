""" class person:

    # -> Propertys
    name = 'shanto'
    occupation = 'software developer'
    networth = 10000

    # -> Methdos
    def info(self):
        print(f"{self.name} is a {self.occupation}")


x_person = person()
a_person = person()
b_person = person()

a_person.name = "Saiful "
a_person.occupation = "Web Devloper"

b_person.name = "Islam "
b_person.occupation = "Web Design & Devloper"

# print(a_person.name, a_person.occupation)


a_person.info()
b_person.info()
x_person.info()  # -> Store Defualt Value """

# *************************************

"""
    * Class     -> একটা মানুষের নাম
    * Object    -> মানুশের কি কি বেষিস্ট আছে সেইটা।
    * self      ->
"""


""" class WaltonUsta:
    #Our New Class Class

    def driving(self):
        run_the_car

    def music(self):
        run_the_music

    def fuel(self):
        lode_the_fuel

    def horn(self):
        make_sound_polliution

 """


# * -----------------------

""" class student:
    roll = ""
    gpa = ""


# 1nd Object
shanto = student()
print(isinstance(shanto, student))
# * isinstance -> Object তেরি হয়েছে কিনা সেইটা চেক করার জন্য এই ফাংশন ব্যবহার হয়।

shanto.roll = 101
shanto.gpa = 3.70


print(f"Roll : {shanto.roll}, GPA : {shanto.gpa}")

# 2nd Object
Saifulshanto = student()
print(isinstance(shanto, student))

Saifulshanto.roll = 102
Saifulshanto.gpa = 4.0

print(f"Roll : {Saifulshanto.roll}, GPA : {Saifulshanto.gpa}") """

# **********************************************


""" class RailWayForm:  # -> Class
    # -> Object In Class
    #* name is Object = "data" is entity
    name = ""
    setNumber = 0
    tiketPrice = 0
    location = ""


p1 = RailWayForm()
p1.name = "Shanto"
p1.setNumber = 31
p1.tiketPrice = 350
p1.location = "Mirpur"

print(
    f"pasensger 01 Information : Name -> {p1.name}, Set Number -> {p1.setNumber}, Tiket Price -> {p1.tiketPrice},location-> {p1.location} "
)

p2 = RailWayForm()
p2.name = "Saiful"
p2.setNumber = 33
p2.tiketPrice = 450
p2.location = "Uttora"

print(
    f"pasensger 02 Information : Name -> {p2.name}, Set Number -> {p2.setNumber}, Tiket Price -> {p2.tiketPrice},location-> {p2.location} "
) """

# *-------------------------------------------


""" class person:
    name = ""
    age = 0


person1 = person()
person1.name = "Saiful"
person1.age = 20
print(f"Person 01 info :- \n\t Name : {person1.name} \n\t age : {person1.age}")

person2 = person()
person2.name = "Shanto"
person2.age = 25
print(f"Person 02 info :- \n\t Name : {person2.name} \n\t age : {person2.age}") """


""" class person:
    name = ""
    age = 0

    def info(self):
        print(
            f"Person 01 info :- \n\t Name : {self.name} \n\t age : {self.age}")


person1 = person()
person1.name = "Saiful"
person1.age = 20
person1.info()

person2 = person()
person2.name = "Shanto"
person2.age = 25
person2.info() """

# *-------------------------------


""" class Calculator:
    def addition(self, a, b):
        return a+b

    def subtraction(self, a, b):
        return a-b

    def multiplication(self, a, b):
        return a*b

    def division(self, a, b):
        try:
            return a/b
        except ZeroDivisionError:
            return 'It is impossible to divide by zero.'

# -> my_calculator is Object
my_calculator = Calculator()

temp = my_calculator.addition(10, 20)
print("addition is : ", temp)

temp = my_calculator.subtraction(10, 20)
print("subtraction is : ", temp)

temp = my_calculator.multiplication(10, 20)
print("multiplication is : ", temp)

temp = my_calculator.division(10, 0)
print("division is : ", temp) """


""" class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a+self.b

    def subtraction(self):
        return self.a-self.b

    def multiplication(self):
        return self.a*self.b

    def division(self):
        try:
            return self.a/self.b
        except ZeroDivisionError:
            return 'It is impossible to divide by zero.'


# -> my_calculator is Object
my_calculator = Calculator(10,5)

temp = my_calculator.addition()
print("addition is : ", temp)

temp = my_calculator.subtraction()
print("subtraction is : ", temp)

temp = my_calculator.multiplication()
print("multiplication is : ", temp)

temp = my_calculator.division()
print("division is : ", temp) """



# The blueprint to create monsters
class Monster:
    def __init__(self, color, heads):
        self.color = color
        self.heads = heads

# Create some real monsters
fogthing = Monster("Black", 5)
mournsnake = Monster("Yellow", 4)
tangleface = Monster("Red", 3)

# Check whether those monsters got different existence in memory or not
print('I have ' + str(fogthing.heads) + ' heads and I\'m ' + fogthing.color)
print('I also have ' + str(mournsnake.heads) + ' heads and I\'m ' + mournsnake.color)
print('I got ' + str(tangleface.heads) + ' heads and I\'m ' + tangleface.color) 