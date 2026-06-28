import os
import time

project = int(input(
    "Which project?\n"
    "1 = Timer\n"
    "2 = Rows/Columns Generator\n"
    "3 = Shopping Cart\n"
    "Choice: "
))



if project == 1:
    realTime = int(input("What's your timer count in seconds? "))

    os.system("clear")
    print("Starting the timer!")

    for x in range(realTime, 0, -1):
        seconds = x % 60
        minutes = (x // 60) % 60
        hours = x // 3600

        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)


elif project == 2:
    rows = int(input("How many rows? "))
    columns = int(input("How many columns? "))
    symbol = input("Pick a symbol/emoji: ")

    os.system("clear")

    for r in range(rows):
        for c in range(columns):
            print(symbol, end="")
        print()

elif project == 3:
    cart = []
    prices = []

    while True:
        os.system("clear")

        food = input("Add a food [b = bill]: ")

        if food.lower() == "b":
            break

        price = input("Enter the price: $")

        if not price.isdigit():
            print("Enter a valid price!")
            time.sleep(1)
            continue

        cart.append(food)
        prices.append(int(price))

        print(f"{food} added to the cart!")
        time.sleep(1)

    os.system("clear")
    print("------ YOUR BILL ------")

    total = 0

    for i in range(len(cart)):
        print(f"{cart[i]} - ${prices[i]}")
        total += prices[i]

    print("-----------------------")
    print(f"Total: ${total}")

# ---------------- INVALID ---------------- #

else:
    print("Invalid project number.")