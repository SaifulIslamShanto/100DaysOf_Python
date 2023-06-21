""" def myFunc():
    print("Hello World")


what_i_GOT = myFunc() #Hello World
print(what_i_GOT) #None """


""" def myFunc(x):
    if x:
        return x*x
    else:
        return 0


# print(myFunc()) #-> ERROR
print(myFunc(5)) """


def myFunc(x=None):
    if x:
        return x*x
    else:
        return 0

print(myFunc())
print(myFunc(5))