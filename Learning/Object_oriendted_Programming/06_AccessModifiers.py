""" 
    * |> Type Of Access Specifiers
    -> Public Access Modifier
    -> Private Access Modifier
    -> Protected Access Modifier
"""

# * |> Public Access Modifier
""" class inFo:
    # -> Constractor Is Defined
    def __init__(self):
        self.name = "SHanto"  # -> Public Variable
        self.age = 23  # -> Public Variable


a = inFo()
print(a.name, a.age) """


# * |> Private Access Modifier

""" class inFo:
    # -> Constractor Is Defined
    def __init__(self):
        self.__name = "SHanto"      # -> Private Variable
        self.__age = 23             # -> Private Variable


a = inFo()
print(a._inFo__name, a._inFo__age)


print(a.__dir__()) #-> Name Mangling """


# * |> Protected Access Modifier


class Student:
    def __init__(self):
        self._name = "Shanto"

    def _funName(self):  # * Protected Method
        return "shantoDevX"


class Subject(Student):  # * inherited Class
    pass


obj = Student()
obj1 = Subject()
print(dir(obj))

# * Calling by object of Student Class
print(obj._name)
print(obj._funName)

# * Calling by object of Subject Class
print(obj1._name)
print(obj1._funName)
