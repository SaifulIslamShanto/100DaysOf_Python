""" primeNumber = int(input("Enter Your Number : "))
if primeNumber == 1:
    print("Not Prime Number")

if primeNumber > 1:
    for i in range(2, primeNumber):
        if (primeNumber % i == 0):
            print("Not Prime Number")
            break
    else:
        print("its Prime Number") """

# * ----------------------------------------------

primeNumbers = int(input("Enter any Number : "))

if (primeNumbers == 1):
    print("Its not a Prime Number")
if primeNumbers > 1:
    for i in range(2, primeNumbers):
        if (primeNumbers % i == 0):
            print("its not a Prime Number")
            break
    else:
        print("Its a Prime Number")
