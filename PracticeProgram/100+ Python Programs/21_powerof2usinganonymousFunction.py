ntrems = int(input("Enter Number of Terms Here : "))

result = list(
    map(
        lambda x: 2 ** x, range(ntrems+1)
    )
)

print(result)

for i in range(ntrems+1):
    print("The value of 2 raised to Power ", i, "is", result[i])
