import random
from hangman_art import HANGMANPICS

word_list = ["aardvark", "baboon", "camel"]
word = list(random.choice(word_list))
placeholder_word = []
number_of_placeholders = len(word)
lives = 7
points = 0
hangman = 0
guessed_letters = []

for i in range(number_of_placeholders):
    placeholder_word.append("_")

print(''.join(placeholder_word))

while lives != 0:
    guess = input("Guess a letter.\n").lower()
    if guess not in guessed_letters:
        if guess in word:
            print("Your guess is correct!")
            guessed_letters.append(guess)
            for i in range(number_of_placeholders):
                if word[i] == guess:
                    placeholder_word[i] = guess
            print(''.join(placeholder_word))
            if placeholder_word == word:
                print("You won!")
                break
        else:
            print("Your guess is incorrect!")
            guessed_letters.append(guess)
            print(HANGMANPICS[hangman])
            hangman += 1
            lives -= 1
            if lives == 0:
                print("You lost!")
                break
    elif guess in guessed_letters:
        print("You already guessed this letter.")

