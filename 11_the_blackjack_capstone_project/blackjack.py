from art import logo
import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def random_choice():
    return random.choice(cards)

while True: 
    # Start game and reset hands
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start_game == "n":
        break
    dealer_hand = []
    player_hand = []
    # First Round
    for i in range(2):
        player_hand.append(random_choice())
    player_score = sum(player_hand)
    for i in range(2):
        dealer_hand.append(random_choice())
    dealer_score = sum(dealer_hand)
    print(f"Your cards: {player_hand}, your current score: {player_score}")
    print(f"Dealer's first card: {str(dealer_hand[0])}")
    if player_score == 21:
        print("You win with a Blackjack!")
        continue
    elif player_score > 21:
        print("You lose!")
        continue
    proceed = input("Type 'y' to get another card, type 'n' to pass: ")
    if proceed == "y":
    # Consecutive Rounds; Player hits as many times as he likes
        while player_score < 21:
            player_hand.append(random_choice())
            player_score = sum(player_hand)
            if player_score >= 21:
                break
            print("\n" * 100)
            print(f"Your cards: {player_hand}, your current score: {player_score}")
            print(f"Dealer's first card: {str(dealer_hand[0])}")
            proceed = input("Type 'y' to get another card, type 'n' to pass: ")
            if proceed == "n":
                break


    # Dealer has to hit if his cards are below 17
    while dealer_score < 17:
        dealer_hand.append(random_choice())
        dealer_score = sum(dealer_hand)

    # Print final hands and score
    print("\n" * 100)
    print(f"Your final hand: {player_hand}, your final score: {player_score}")
    print(f"Dealer's final hand: {dealer_hand}, dealer's final score: {dealer_score}")

    # End Evaluation
    if player_score > 21:
        print("You lose!")
    elif player_score < 21:
        if player_score == dealer_score:
            print("Draw.")
        elif dealer_score > 21:
            print("You win.")
        elif player_score < dealer_score:
            print("You lose!")
        elif player_score > dealer_score:
            print("You win!")
    elif player_score == 21:
        print("You win with a Blackjack!")
    elif player_score > 21:
        print("You lose!")

        






