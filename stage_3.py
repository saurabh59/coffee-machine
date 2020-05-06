print("Write how many ml of water the coffee machine has:")
wa = int(input())
print("Write how many ml of milk the coffee machine has:")
ma = int(input())
print("Write how many grams of coffee beans the coffee machine has:")
ca = int(input())
print("Write how many cups of coffee you will need:")
needed = int(input())
k = min(wa // 200, ma // 50, ca // 15)
if k == needed:
    print("Yes, I can make that amount of coffee")
elif k > needed:
    print("Yes, I can make that amount of coffee (and even", k - needed, "more than that)")
else:
    print("No, I can make only", k, "cups of coffee")
    
