class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cups = 9
        self.money = 550
        self.action = ''
    def main_menu(self):
        print("Write action (buy, fill, take, remaining, exit):")
        try:
            self.action = input()
        except:
            pass
        if self.action == "exit":
            return
        elif self.action == "buy":
            self.coffee_menu()
        elif self.action == "fill":
            self.fill()
        elif self.action == "take":
            self.take()
        elif self.action == "remaining":
            self.remaining()
    def coffee_menu(self):
        print("")
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        self.action = input()
        if self.action == "1":
            self.espresso()
        elif self.action == "2":
            self.latte()
        elif self.action == "3":
            self.cappuccino()
        else:
            self.main_menu()
    def cappuccino(self):
        if self.water >= 200:
            if self.milk >= 100:
                if self.coffee >= 12:
                    if self.cups >= 1:
                        print("I have enough resources, making you a coffee!")
                        print("")
                        self.water -= 200
                        self.milk -= 100
                        self.coffee -= 12
                        self.cups -= 1
                        self.money += 6
                        self.main_menu()
                    else:
                        print("Sorry, not enough disposable cups!")
                        print("")
                else:
                    print("Sorry, not enough coffe beans!")
                    print("")
            else:
                print("Sorry, not enough milk!")
                print("")
        else:
            print("Sorry, not enough water!")
            print("")
        self.main_menu()
    def latte(self):
        if self.water >= 350:
            if self.milk >= 75:
                if self.coffee >= 20:
                    if self.cups >= 1:
                        print("I have enough resources, making you a coffee!")
                        print("")
                        self.water -= 350
                        self.milk -= 75
                        self.coffee -= 20
                        self.cups -= 1
                        self.money += 7
                        self.main_menu()
                    else:
                        print("Sorry, not enough disposable cups!")
                        print("")
                else:
                    print("Sorry, not enough coffe beans!")
                    print("")
            else:
                print("Sorry, not enough milk!")
                print("")
        else:
            print("Sorry, not enough water!")
            print("")
        self.main_menu()
    def espresso(self):
        if self.water >= 250:
            if self.coffee >= 16:
                if self.cups >= 1:
                    print("I have enough resources, making you a coffee!")
                    print("")
                    self.water -= 250
                    self.coffee -= 16
                    self.cups -= 1
                    self.money += 4
                    self.main_menu()
                else:
                    print("Sorry, not enough disposable cups!")
                    print("")
            else:
                print("Sorry, not enough coffe beans!")
                print("")
        else:
            print("Sorry, not enough water!")
            print("")
        self.main_menu()
    def fill(self):
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
        self.water += water_add
        self.milk += milk_add
        self.coffee += coffee_add
        self.cups += cups_add
        self.main_menu()
    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0
        print("")
        self.main_menu()
    def remaining(self):
        print("")
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"${self.money} of money")
        print("")
        self.main_menu()

k = CoffeeMachine()
k.main_menu()
