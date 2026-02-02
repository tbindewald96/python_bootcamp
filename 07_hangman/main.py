import random
from hangman_art import HANGMANPICS

word_list = ["aardvark", "baboon", "camel"]
placeholder_word = []
hangman = HANGMANPICS[0]
lives = 7
word = random.choice(word_list)

#Create placeholder with same number of blanks as choice

number_of_placeholders = len(word)

for i in range(number_of_placeholders):
    placeholder_word.append("_")

print(placeholder_word)

guess = input("Guess a letter.\n").lower()

while lives != 0:
    if guess in word:
        print("Your guess is correct!")
        location_of_letter = word.find(guess)
        placeholder_word[location_of_letter] = guess
        print(placeholder_word)
    else:
        print("Your guess is incorrect!")
        lives -= 1
        print(hangman)

print("You lost!")


# Create a display with letter at correct location

