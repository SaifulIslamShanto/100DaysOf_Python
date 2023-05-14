# pyhton DocString
""" _summary_

    Args:
        n (_type_): _description_
    """


def square(n):
    """
Taks in a numnber n, Returns the square of n
    """
    print(n**2)


square(5)
print(square.__doc__)
