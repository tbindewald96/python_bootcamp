from art import logo
import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_hand = []
player_hand = []

#The deck is unlimited in size.
#There are no jokers.
#The Jack/Queen/King all count as 10.
#The Ace can count as 11 or 1.
#Use the following list as the deck of cards:
#The cards in the list have equal probability of being drawn.
#Cards are not removed from the deck as they are drawn.
#The computer is the dealer.

#input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

def random_choice():
    return random.choice(cards)

for i in range(2):
    player_hand.append(random_choice())

player_score = sum(player_hand)

computer_first_card = random_choice()
computer_hand.append(computer_first_card)

print(f"Your cards: {player_hand}, current score: {player_score}")
print(f"Computer's first card: {computer_first_card}")
