""" letter = "Hey my name is {} and I am from{}"
countery = "Bangladesh"
name = "Shanto"

print(letter.format(name, countery)) """
countery = "Bangladesh"
name = "Shanto"
print(f"Hey my name is {name} and I am from{countery}")
print(f"Hey my name is {{name}} and I am from{{countery}}")

print(type(f"{2*30}"))

# https://realpython.com/python-f-strings/