from treasure import trove

print(trove)
print("Welcome to Treasure Island.\nYour mission is to find the treasure.\nYou're at a cross road. Where do you want to go?")
decision1 = input('Type "left" or "right"\n').lower()
if decision1 == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    decision2 = input('Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if decision2 == "wait":
        print('You are standing in front of two doors.')
        decision3 = input('Type "right" or "left".\n').lower()
        if decision3 == "right":
            print("You found the treasure. You won!")
        else:
            print("You opened the lions cage. You died.")
    else:
        print("You have been eaten by crocodiles.")
else: 
    print("You ran into a bunch of highwaymen. You died.")



