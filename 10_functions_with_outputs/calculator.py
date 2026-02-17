from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(logo)

n1 = int(input("Type the first number: "))

while True:
    operator = input('Chose the operation: "+", "-", "*" or "/" ') 
    n2 = int(input("Type the next number: "))
    result = operations[operator](n1, n2)
    print(f"Result: {result}")
    proceed = input('Do you want to continue? Type "yes" or "no" ').lower()
    if proceed == "no":
        n1 = int(input("Type the first number: "))
    else:
        n1 = result