
# * soluation 1
# -> 1KM to 0.621371 Miles

""" km = float(input("Enter Your Value In KMS : "))
miles = km*0.621371
print(km, "KMS WIll BE : ", miles, " miles")
 """

# * soluation 2


def kmToMiles():
    return km*0.621371


km = float(input("Enter Your Value In KMS : "))
print(km, "KMS WIll BE : ", kmToMiles(), "Miles")
