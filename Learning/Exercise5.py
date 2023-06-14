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

import random

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
