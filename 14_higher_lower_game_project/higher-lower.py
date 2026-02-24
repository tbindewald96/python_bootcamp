from art import *
from gamedata import data 
import random

score = 0

print(logo)

while True:
    candidate_a = random.choice(data)
    candidate_b = random.choice(data)

    while candidate_a == candidate_b:
        b = random.choice(data)

    if candidate_a["follower_count"] > candidate_b["follower_count"]:
        winner = "a"
    else:
        winner = "b"

    print(f"Compare A: {candidate_a['name']}, a {candidate_a['description']}, from {candidate_a['country']}.")
    print(vs)
    print(f"Compare B: {candidate_b['name']}, a {candidate_b['description']}, from {candidate_b['country']}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 100)
    print(logo)

    if guess == winner:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        break



