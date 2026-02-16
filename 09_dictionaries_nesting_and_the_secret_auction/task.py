from art import logo

bid_dictionary = {}
done = False
floor_value = 0

print(logo)
print("Welcome to the secret auction program.")

while not done: 
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    bid_dictionary[name] = bid
    proceed = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if proceed == "no":
        done = True
    print("\n" * 100)   

for key in bid_dictionary:
    if bid_dictionary[key] > floor_value:
        floor_value = bid_dictionary[key]

bid = floor_value
name_list = [key for key, val in bid_dictionary.items() if val == bid]
name = name_list[0]

print(f"The winner is {name} with a bid of ${bid}.")