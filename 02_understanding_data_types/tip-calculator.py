print("Welcome to the tip calculator!")
total = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
persons = int(input("How many people to split the bill? "))

result = round(((total * (1 + (tip / 100))) / persons),2)

print(f"Each person should pay: ${result}")