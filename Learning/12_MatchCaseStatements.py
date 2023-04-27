# Match Case Statements
# -> Same a SwitchCase

x = int(input("Enter the value of x : "))
match x:
    # if x is 0
    case 0:
        print("x is zero")
    case 1:
        print("X is ONE")
    case 4:
        print("Case is 4")

    # -> case with if condition
    case _ if x != 90:  # -> Deafult
        print(x, "is not 90")
    case _ if x != 80:  # -> Deafult
        print(x, "is not 80")
    case _:  # -> Deafult
        print(x)
