qustainIs = "Which Country Do you Live ?"
print(qustainIs)
ansListIs = ["0. Bangladesh", "1. India", "2. USA", "3. Englend"]
print(ansListIs)

index = input("Enter The ANS 0 to 3 : ")
index = int(index)
AnsIs = ansListIs[index]

if (AnsIs == "0. Bangladesh"):
    print("The COuntry Is : ", AnsIs)
    print("Its Correct")
else:
    print("The COuntry Is : ", AnsIs)
    print("Its Wrong")
