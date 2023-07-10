
# * উত্তরাধিকার সূত্রে প্রাপ্ত কোনো কিছুকে ইনহেরিট্যান্স বলে

""" class Emplooyee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The Name of Employee :  {self.id} is {self.name}")


class programmer(Emplooyee):

    def showLanguage(self):
        print("The Default language is python")


emp1 = Emplooyee("Shanto", 400)
emp1.showDetails()

emp2 = Emplooyee("saiful", 401)
emp2.showDetails()

emp3 = programmer("islam", 403)
emp3.showLanguage() """

# ---------------------------------------


""" class Calculator:
    #Do addition, subtraction, multiplication, division, square and cube.

    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return 'It is impossible to divide by zero.'


class SuperCalculator(Calculator):
    # Child class of Calculator. Do square and cube.

    def square(self, a):
        return a * a

    def cube(self, a):
        return a * a * a


my_calculator = SuperCalculator()

temp = my_calculator.addition(23, 47)
print(temp)

temp = my_calculator.subtraction(87, 54)
print(temp)

temp = my_calculator.multiplication(65, 56)
print(temp)

temp = my_calculator.division(852, 76)
print(temp)

temp = my_calculator.square(7)
print(temp)

temp = my_calculator.cube(3)
print(temp)
 """

# ----------------------------------------------------


""" class cutomError(Exception):
    # Just For Example

    def __init__(self, message):
        self.message = message


try:
    raise cutomError("Its Is A Custom Error")
except cutomError as e:
    print(e) """


# class Calculator:
#     """Do addition, subtraction, multiplication and division."""

#     def addition(self, a, b):
#         return a + b

#     def subtraction(self, a, b):
#         return a - b

#     def multiplication(self, a, b):
#         return a * b

#     def division(self, a, b):
#         try:
#             return a / b
#         except ZeroDivisionError:
#             return 'It is impossible to divide by zero.'


# class SuperCalculator(Calculator):
#     """Do addition, subtraction, multiplication, division, square and cube."""

#     def addition(self, a, b, c):
#         return a + b + c

#     def square(self, a):
#         return a * a

#     def cube(self, a):
#         return a * a * a


# my_calculator = SuperCalculator()

# temp = my_calculator.addition(23, 47, 12)
# print(temp)

# temp = my_calculator.subtraction(87, 54)
# print(temp)

# temp = my_calculator.multiplication(65, 56)
# print(temp)

# temp = my_calculator.division(852, 76)
# print(temp)

# temp = my_calculator.square(7)
# print(temp)

# temp = my_calculator.cube(3)
# print(temp)



class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        return self.a + self.b
    def Substraction(self):
        return self.a - self.b
    def Multiplication(self):
        return self.a * self.b
    def Division(self):
        try:
            return self.a/self.b
        except ZeroDivisionError:
            return "The number can not be divided by 0"

class Supercalculator(Calculator):
    def __init__(self, a, b,c):
        super().__init__(a, b)
        self.c=c
    def squre(self):
        return self.c * self.c
    def cube(self):
        return self.c * self.c * self.c
        

A=int(input("GIVE NUMBER 1: "))
B=int(input("GIVE NUMBER 2: "))
C=int(input("GIVE NUMBER 3: "))
MYCALCULATOR=Supercalculator(A,B,C)
temp=MYCALCULATOR.addition()
print(A,"+",B,"= ",temp)
temp=MYCALCULATOR.Substraction()
print(A,"-",B,"= ",temp)
temp=MYCALCULATOR.Multiplication()
print(A,"*",B,"= ",temp)
temp=MYCALCULATOR.Division()
print(A,"/",B,"= ",temp)
temp=MYCALCULATOR.squre()
print(C,"*",C,"= ",temp)
temp=MYCALCULATOR.cube()
print(C,"*",C,"*",C,"= ",temp)