def fib(n):
    serise = []
    a, b = 0, 1
    while b < n:
        serise.append(b)
        a, b = b, a+b
    return serise


if __name__ == "__main__":
    temp = fib(20)
    print(temp)
