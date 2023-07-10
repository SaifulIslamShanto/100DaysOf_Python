

""" class myClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value IS : {self._value}")

    @property
    def ten_value(self):
        return 10 * self._value

    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value/10


obj = myClass(10)
obj.ten_value = 57
print(obj.ten_value)
obj.show() """

# ************ ->

# * গেটার মেথড একটি অ্যাট্রিবিউটের মান রিটার্ন করে। এটি অ্যাট্রিবিউটের মান পড়ার জন্য ব্যবহার করা হয়। সাধারণত গেটার মেথডের নাম হয় "get_" এবং অ্যাট্রিবিউটের নাম পরে আসে

""" class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self): #* Getter Method
        return self._name


person = Person("Shanto")
name = person.get_name()
print(name) """


class Person:
    def __init__(self, name):
        self._name = name

    # @property
    def get_name(self): #* Getter Method
        return self._name


person = Person("Shanto")
name = person.get_name()
print(name)


# * সেটার মেথড একটি অ্যাট্রিবিউটের মান পরিবর্তন করে। এটি অ্যাট্রিবিউটের মান লিখতে ব্যবহার করা হয়। সাধারণত সেটার মেথডের নাম হয় "set_" এবং অ্যাট্রিবিউটের নাম পরে আসে
#* SkIP FOR NOW