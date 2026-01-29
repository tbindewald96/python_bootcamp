from lettersNumbersSymbols import letters
from lettersNumbersSymbols import numbers
from lettersNumbersSymbols import symbols
import random

print("Welcome to the PyPassword Generator!")
numberOfLetters = int(input("How many letters would you like in your password?\n"))
numberOfSymbols = int(input("How many symbols would you like?\n"))
numberOfNumbers = int(input("How many numbers would you like?\n"))

listOfItems = []

for i in range(0, numberOfLetters):
    listOfItems.append(letters[random.randint(0, len(letters)-1)])

for i in range(0, numberOfSymbols):
    listOfItems.append(symbols[random.randint(0,len(symbols)-1)])

for i in range(0, numberOfNumbers):
    listOfItems.append(numbers[random.randint(0,len(numbers)-1)])

password = str()

count = len(listOfItems)


for i in range(count):
    item = random.choice(listOfItems)
    listOfItems.remove(item)
    password += item

print(f"Your password is: {password}")