""" import time

timesTamp = time.strftime('%H:%M:%S')
print(timesTamp)
timesTamp = time.strftime('%H')
print(timesTamp)
timesTamp = time.strftime('%M')
print(timesTamp)
timesTamp = time.strftime('%S')
print(timesTamp) """

# https://docs.python.org/3/library/time.html#time.strftime

import time

timesTamp = time.strftime('%H:%M:%S')
print("Now Time Is : ", timesTamp)
hour = int(time.strftime('%H'))
print(hour)

if (hour >= 0 and hour < 12):
    print("Good Morning")
elif (hour >= 12 and hour < 17):
    print("Good AfterNoon Sir")
elif (hour >= 17 and hour <= 0):
    print("Good Night")
