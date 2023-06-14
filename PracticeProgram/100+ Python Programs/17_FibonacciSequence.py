""" def fibonacci(n):
    fib = [0, 1]  # প্রথম দুটি সংখ্যা
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])  # প্রাক্তন দুটি সংখ্যার যোগফল
    return fib

n = int(input("কতগুলো সংখ্যা চান ফিবোনাচ্চি শ্রেণীতে দেখতে? "))
result = fibonacci(n)
print(result)
 """

#  ----------------------
a = 0
b = 1
num = int(input("Enter a Number : "))

if num == 1:
    print(a)
else:
    print(a)
    print(b)
    # for i in range(1, num+1):
    for i in range(2, num):
        c = a+b
        a = b
        b = c
        print(c)
