from hands import *
import random

choice = int(input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choice == 0:
    print(rock)
    print("You chose rock.")
elif choice == 1:
    print(paper)
    print("You chose paper.")
else:
    print(scissors)
    print("You chose scissors.")

opponent_choice = random.randint(0,2)

if opponent_choice == 0:
    print(rock)
    print("Your opponent chose rock.")
elif opponent_choice == 1:
    print(paper)
    print("Your opponent chose paper.")
else:
    print(scissors)
    print("Your opponent chose scissors.")

if choice == 0:
    if opponent_choice == 0:
        print("Draw!")
    elif opponent_choice == 1:
        print("You lose!")
    else: 
        print("You won!")
elif choice == 1:
    if opponent_choice == 0:
        print("You won!")
    elif opponent_choice == 1:
        print("Draw!")
    else:
        print("You lose!")
else:
    if opponent_choice == 0:
        print("You lose!")
    elif opponent_choice == 1:
        print("You won!")
    else:
        print("Draw!")