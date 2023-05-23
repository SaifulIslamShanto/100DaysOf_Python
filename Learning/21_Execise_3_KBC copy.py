""" qustainIs = "Which Country Do you Live ?"
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
 """

# -> Solution

questions = [
    ["Which language was used to create Facebook >",
     "python", "Javascript", "php", "None", 4],
    ["Which language was used to create Facebook >",
     "python", "Javascript", "php", "None", 4],
    ["Which language was used to create Facebook >",
     "python", "Javascript", "php", "None", 4],
    ["Which language was used to create Facebook >",
     "python", "Javascript", "php", "None", 4],
    ["Which language was used to create Facebook >",
     "python", "Javascript", "php", "None", 4],
    ["Which language was used to create Facebook >",
     "python", "Javascript", "php", "None", 4],
    ["Which language was used to create Facebook >",
     "python", "Javascript", "php", "None", 4],
    ["Which language was used to create Facebook >",
     "python", "Javascript", "php", "None", 4],
    ["Which language was used to create Facebook >",
     "python", "Javascript", "php", "None", 4],
    ["Which language was used to create Facebook >",
     "python", "Javascript", "php", "None", 4],
    ["Which language was used to create Facebook >",
     "python", "Javascript", "php", "None", 4],
    ["Which language was used to create Facebook >",
     "python", "Javascript", "php", "None", 4]

]

lavels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000,]
money = 0
for i in range(0, len(questions)):
    # * IN question DataStrod <----< from questions[i]
    question = questions[i]
    print(f"\n\nQustion for Taka.{lavels[i]}")
    print(f"a.{question[1]}        b.{question[2]}")
    print(f"c.{question[3]}        d.{question[4]}")

    reply = int(input("Enter Your Answer (1-4) or 0 to Quit : "))
    if (reply == 0):
        money = lavels[i-1]
        break
    if (reply == question[-1]):
        print(f"Correct Answer, your have won Taka. {lavels[i]}")
        if (i == 4):
            money = 10000
        elif (i == 9):
            money = 32000
        elif (i == 14):
            money = 10000000
    else:
        print("wrong Answer!")
        break

print(f"Your Take Home Money is {money}")
