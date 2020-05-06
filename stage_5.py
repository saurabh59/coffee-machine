water_av = 400
milk_av = 540
coffee_av = 120
cups_av = 9
money_av = 550
while True:
    print("Write action (buy, fill, take, remaining, exit):")
    i = input()
    if i == "buy":
        print("")
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        coffee_op = input()
        if coffee_op == "1":
            if water_av >= 250 and coffee_av >= 16:
                print("I have enough resources, making you a coffee!")
                print("")
                water_av -= 250
                coffee_av -= 16
                money_av += 4
                cups_av -= 1
            else:
                if water_av < 250:
                    print("Sorry, not enough water!")
                    print("")
                else:
                    print("Sorry, not enough coffee beans!")
                    print("")
        if coffee_op == "2":
            if water_av >= 350 and milk_av >= 75 and coffee_av >= 20:
                print("I have enough resources, making you a coffee!")
                print("")
                water_av -= 350
                milk_av -= 75
                coffee_av -= 20
                cups_av -= 1
                money_av += 7
            else:
                if water_av < 350:
                    print("Sorry, not enough water!")
                    print("")
                elif milk_av < 75:
                    print("Sorry, not enough milk!")
                    print("")
                elif coffee_av < 20:
                    print("Sorry, not enough coffe beans!")
                    print("")
                else:
                    print("Sorry, not enough disposable cups!")
                    print("")
        if coffee_op == "3":
            if water_av >= 200 and milk_av >= 100  and coffee_av >= 12:
                print("I have enough resources, making you a coffee!")
                print("")
                water_av -= 200
                milk_av -= 100
                coffee_av -= 12
                cups_av -= 1
                money_av += 6
            else:
                if water_av < 200:
                    print("Sorry, not enough water!")
                    print("")
                elif milk_av < 100:
                    print("Sorry, not enough milk!")
                    print("")
                elif coffee_av < 12:
                    print("Sorry, not enough coffe beans!")
                    print("")
        continue
        if coffee_op == "back":
            print("")
            continue
    if i == "take":
        print("I gave you", money_av)
        print("")
        money_av = 0
        continue
    if i == "fill":
        print("")
        print("Write how many ml of water do you want to add:")
        water_add = int(input())
        print("Write how many ml of milk do you want to add:")
        milk_add = int(input())
        print("Write how many grams of coffee beans do you want to add:")
        coffee_add = int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        cups_add = int(input())
        print("")
        water_av += water_add
        milk_av += milk_add
        coffee_av += coffee_add
        cups_av += cups_add
        continue
    if i == "remaining":
        print("The coffee machine has:")
        print(water_av, "of water")
        print(milk_av, "of milk")
        print(coffee_av, "of coffee beans")
        print(cups_av, "of disposable cups")
        print("$",money_av, "of money")
        print("")
        continue
    if i == "exit":
        break








