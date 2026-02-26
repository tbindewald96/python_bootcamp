MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins_value = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.1,
    "quarter": 0.25,
}

coins_amount = {
    "penny": 1,
    "nickel": 1,
    "dime": 1,
    "quarter": 1, 
}

def budget():
  coins = ["penny", "nickel", "dime", "quarter"]
  values = []
  for i in coins:
    values.append(coins_amount[i] * coins_value[i])
  return round(sum(values), 2)


# TODO: 1. Print report of all resources
# TODO: 2. Check resources sufficient to make order
# TODO: 3: Process coins

while True:
    button = input("What would you like? (espresso/latte/cappuccino): ")

    if button == "report":
            print(f"Water: {resources["water"]}ml")
            print(f"Milk: {resources["milk"]}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${budget()}")
    elif button == "espresso" or button == "latte" or button == "cappucino":
        
    elif button == "off":
        break

