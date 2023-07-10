""" def hello():
    print("Hello World")

hello() """

""" def get_int_as_str(number):
    return str(number)

def print_int(my_function, number):
    print(my_function(number))
    return

print_int(get_int_as_str, 130) """

# ->


""" def greet(fx):
    def mfx():
        print("GOOD MORNING!")
        fx()
        print("Thanks for using This fucntion")
    return mfx


@greet
def hello():
    print("Hello World")


hello() """


""" def greet(fx):
    def mfx(*args, **kwargs):
        print("GOOD MORNING!")
        fx(*args, **kwargs)
        print("Thanks for using This fucntion")
    return mfx

@greet
def hello():
    print("Hello World")

@greet
def add(a, b):
    print(a+b)

# greet(hello)()
hello()
# greet(add)(1,2)
add(1, 21) """


""" def greet(fx):
    # def mfx(*args, **kwargs):
    def mfx():
        print("GOOD MORNING!")
        # fx(*args, **kwargs)
        fx()
        print("Thanks for using This fucntion")
    return mfx


@greet
def hello():
    print("Hello World")


hello() """

""" @greet
def add(a, b):
    print(a+b) """

# greet(hello)()
# hello()
# greet(add)(1,2)
# add(1, 21)

# *-*************


""" def Pinfo(fx):
    def mPinfo():
        print("\n")
        print("Hello World")
        fx()
        print("Nice")
    return mPinfo


@Pinfo
def hello():
    print("Hello Python")


@Pinfo
def hello2():
    print("Hello Javascript")


hello()
hello2() """

# ***********************************************
""" def get_int_as_str(number):
    return str(number)

def print_int(my_function, number):
    print(my_function(number))
    return

print_int(get_int_as_str, 130) """

""" def get_int_as_str(number):
    print(str(number))
    return

def print_int(my_function, number):
    return my_function(number)

print_int(get_int_as_str, 130) """


""" def print_int(number):
    def get_int_as_str(number):
        print(str(number))
        return

    get_int_as_str(number)
    return """

""" def print_int(number):
    def get_int_as_str(number):
        print(str(number))
        return
    
    return get_int_as_str(number)

print_int(130) """


""" def print_int(my_function):

    def any_function():
        return my_function

    return any_function()


@print_int
def get_int_as_str(number):
    print(str(number))
    return


get_int_as_str(130) """

# ->1
""" def test1():
    print("In test")


test2 = test1
del test1
test2() """

# -> 2 | Return Multiple function in One Function
""" def test(num):
    if (num == 0):
        return print
    if (num == 1):
        return sum


# rest = test(1)
rest = test(0)
print(rest) """

# -> 3 |> function access in function As a argument
""" def test(func1):
    func1("In Test Function")

test(print) """

# -> 4 |> Decorators


""" def test1(func):
    def exec():
        print("First Line of EXEC")
        func()
        print("3rd Line of EXEC")
    return exec


@test1
def my_func():
    print("Learning Python Decorator")


# my_func = test1(my_func)
my_func() """

# https://www.youtube.com/watch?v=lZ42mShq96k
# https://python.howtocode.dev/func-prog/decorator


def mainFunc(func):
    def decoFunc():
        print("My Name Is")
        func()
        print("I'm A Python Developer")
    return decoFunc


@mainFunc
def main2Func():
    print("Saiful Islam Shanto")


main2Func()
