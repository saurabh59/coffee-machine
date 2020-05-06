print("""The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
550 of money""")
print()
print("Write action (buy, fill, take):")
s = input()
if s == "buy":
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    coffee_option = int(input())
    print()
    if coffee_option == 1:
        print("""The coffee machine has:
150 of water
540 of milk
104 of coffee beans
8 of disposable cups
554 of money""")
    elif coffee_option == 2:
        print("""The coffee machine has:
50 of water
465 of milk
100 of coffee beans
8 of disposable cups
557 of money""")
    elif coffee_option == 3:
        print("""The coffee machine has:
200 of water
440 of milk
108 of coffee beans
8 of disposable cups
556 of money""")
elif s == "fill":
    print("Write how many ml of water do you want to add:")
    water_fill = int(input())
    print("Write how many ml of milk do you want to add:")
    milk_fill = int(input())
    print("Write how many grams of coffee beans do you want to add:")
    coffee_fill = int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    cups_fill = int(input())
    print()
    print("The coffee machine has:")
    print(400 + water_fill, "of water")
    print(540 + milk_fill, "of milk")
    print(120 + coffee_fill, "of coffee beans")
    print(9 + cups_fill, "of disposable cups")
    print("550 of money")
elif s == "take":
    print("I gave you $550")
    print()
    print("""The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
0 of money""")
        
