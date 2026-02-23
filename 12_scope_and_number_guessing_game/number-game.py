from random import *
from art import logo
number = randint(1,100)

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    lives = 10
else:
    lives = 5

while lives != 0:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess < number:
        print("Too low.")
        lives -= 1
    elif guess > number:
        print("Too high.")
        lives -=1
    else:
        print(f"You got it! The answer was {number}.")
        break
    if lives == 0:
        print("You run out of guesses. Refresh the page to run again.")
        break
    print("Guess again.")
    