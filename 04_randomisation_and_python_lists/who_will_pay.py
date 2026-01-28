import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

length = len(friends) - 1

person = random.randint(0, length)

print(f"{friends[person]} will pay today.")

