
"""
# Explicit Conversion Typecasting
 a = "1"
b = "2"
print(int(a)+int(b))

# Implicit Conversion Typecasting
c = 1.9
d = 8
print(c+d); 

"""


string = "15"
number = 7
# throws an error if the string is not a valid integer
string_number = int(string)
sum = number + string_number
print("The Sum of both the numbers is: ", sum)


# Python automatically converts
# a to int
a = 7
print(type(a))

# Python automatically converts b to float
b = 3.0
print(type(b))

# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))
