# for Loop with else in Python | Python Tutorial - Day #35

""" for i in range(5):
    print(i)
else:
    print("Sorry No i") """

""" for i in []:
    print(i)
else:
    print("Sorry No i") """

""" for i in range(6):
    print(i)
    # if i == 4:
    #     break
    if i == 4:
        continue
else:
    print("Sorry No i") """

# -> while Loop with Else

i = 0
while (i < 7):
    print(i)
    i = i+1

    if i == 4:
        break
else:
    print("Sorry No i")

""" 
    * এখানে লুপ শেষ হলে else এর ভেলু প্রিন্ট করবে
    * যদি লুপ শেষ না হয়ে break করা হয় তাহলে লুপ শেষ হবে না    এবং else এর ভেলু প্রিন্ট করবে না।
"""
