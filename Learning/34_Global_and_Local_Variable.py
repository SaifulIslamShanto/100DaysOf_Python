# Local vs Global Variables in Python| Python Tutorial - Day #48


""" globVar = 4  # * Global Variable


def LocalVarInsideFunction():

    localVar = 5  # * Local Variable
    print("Local Variable is ", localVar)
    print("Global Variable Inside Function : ", globVar)


print("Global Variable Is : ", globVar)
LocalVarInsideFunction()
# print(localVar)  # *Error Local Variable """

# --------------------------------------------------

globVar = 10  # *Global variable


def my_function():
    global globVar
    globVar = 100
    localVar = 5  # *local variable
    print(localVar)


my_function()
print(globVar)
