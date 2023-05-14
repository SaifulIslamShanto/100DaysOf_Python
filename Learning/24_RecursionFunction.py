# Recursion in Python | Python Tutorial - Day #30

# Factorial
""" 
def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)


num = 5
print("the Factorial of ", num, "is", factorial(num))
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1 """


# -> Fibonacci Serise

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))


number = int(input("Enter the number : "))
print("Fibonacci Sequence")
for i in range(number):
    print(fibonacci(i))
