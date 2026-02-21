from art import logo
import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_hand = []
player_hand = []
done = ()

def random_choice():
    return random.choice(cards)

start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if start_game == "y":
    done == True

# First Round
for i in range(2):
    player_hand.append(random_choice())
player_score = sum(player_hand)
for i in range(2):
    computer_hand.append(random_choice())
computer_score = sum(computer_hand)
print(f"Your cards: {player_hand}, current score: {player_score}")
print(f"Computer's first card: {str(computer_hand[0])}")

# Consecutive Rounds; Player hits as many times as he likes
while player_score < 21 and not done:
    proceed = input("Type 'y' to get another card, type 'n' to pass: ")
    if proceed == "n":
        done = True
    player_hand.append(random_choice())
    player_score = sum(player_hand)
    print(f"Your cards: {player_hand}, current score: {player_score}")
    print(f"Computer's first card: {str(computer_hand[0])}")

# Dealer has to hit if his cards are below 17

while computer_score < 17:
    computer_hand.append(random_choice())
    computer_score = sum(computer_hand)

# End Evaluation
if player_score == 21:
    print("You won!")
elif player_score == computer_score and player_score <= 21:
    print("Draw.")
elif player_score > 21:
    print("You lose!")

        






