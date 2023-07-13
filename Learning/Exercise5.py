# Snake Water Gun
# -> Practice MySelf
""" print("Welcome Snake Water Gun")
print("-------------------------")

computer = input("Your Turn Computer (S,W,G) : ")
player = input("Your Turn player (S,W,G) : ")


s = "snack"
w = "water"
g = "gun"

if ((computer == "s") and (player == "s") or (computer == "w") and (player == "w") or (computer == "g") and (player == "g")):
    print("Drow")
elif ((computer == "s") and (player == "w") or (computer == "g") and (player == "s") or (computer == "w") and (player == "g")):
    print(f"computer win & player Loss")
elif ((computer == "w") and (player == "s") or (computer == "s") and (player == "g") or (computer == "g") and (player == "w")):
    print(f"player win & computer Loss")
elif ((computer == "w") and (player == "s") or (computer == "s") and (player == "g") or (computer == "g") and (player == "w")):
    print(f"player win & computer Loss")
elif ((computer == "s") and (player == "w") or (computer == "g") and (player == "s") or (computer == "w") and (player == "g")):
    print(f"computer win & player Loss")
else:
    print("Error") """


# ***********************************************************************************************************************************

""" import random

options = ["Snack", "Water", "Gun"]
print("Welcome To Snake, Water, Gun Game")
game_results = [
    {
        "option": options,
        "Result": ["Draw", "Win", "Lose"]
    },
    {
        "option": options,
        "Result": ["Draw", "Win", "Lose"]
    },
    {
        "option": options,
        "Result": ["Draw", "Win", "Lose"]
    },
]


try:
    player = int(input("Select Your Character [1. Snack 2. Water 3. Gun ] : "))
    player_Index = player-1
    player_choice = options[player_Index]

    # ->https://www.w3schools.com/python/ref_random_choice.asp
    computer_choice = random.choice(options)
    computer_index = game_results[player_Index]["option"].index(
        computer_choice)

    print(f"You Selected {player_choice}")
    print(f"Computer have Selected {computer_choice}")
    print("You Have", game_results[player_Index]["Result"][computer_index])

except Exception:
    print("Try Again, Select Valid Option")
 """

#  ----------------------------------------------------------------


""" 
import random
def check(comp, user):
    if comp == user:
        return 0
    if (comp == 0 and user == 1):
        return -1
    if (comp == 1 and user == 2):
        return -1
    if (comp == 2 and user == 0):
        return -1

    return 1


comp = random.randint(0, 2)
user = int(input("0 for Snake, 1 for Water and 2 for Gun \n"))

print("You : ", user)
print("Computer : ", comp)

score = check(comp, user)
if (score == 0):
    print("its a Draw")
elif score == -1:
    print("You Lose")
else:
    print("you WON")
 """


# -> Get input From User & Computer




import random  # -> For Random Number
def check(computerInput, userInput):
    if computerInput == userInput:
        return 0
    if computerInput == 0 and userInput == 1:
        return -1
    if computerInput == 1 and userInput == 2:
        return -1
    if computerInput == 2 and userInput == 0:
        return -1

    return 1


computerInput = random.randint(0, 2)
userInput = int(input("0. For Snack \n1. For Water \n2. For Gun \n:- "))

print("User Input : ", userInput)
print("Computer Input : ", computerInput)


score = check(computerInput, userInput)

if (score == 0):
    print("Its a Draw")
elif (score == -1):
    print("You LOSE")
else:
    print("You WIN")
