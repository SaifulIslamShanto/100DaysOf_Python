""" for i in range(10, 0, -2):
    print(i)
# step size -2 """


def floatRange(start, stop, step):
    i = start
    while (i < stop):
        yield i
        i += step


for i in floatRange(0.5, 1.0, 0.1):
    print(i)
