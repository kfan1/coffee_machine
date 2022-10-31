import data

def water_used(cof):
    if cof == "esp":
        return data.MENU["espresso"]["ingredients"]["water"]
    if cof == "lat":
        return data.MENU["latte"]["ingredients"]["water"]
    if cof == "cap":
        return data.MENU["cappuccino"]["ingredients"]["water"]

def coffee_used(cof):
    if cof == "esp":
        return data.MENU["espresso"]["ingredients"]["coffee"]
    if cof == "lat":
        return data.MENU["latte"]["ingredients"]["coffee"]
    if cof == "cap":
        return data.MENU["cappuccino"]["ingredients"]["coffee"]

def milk_used(cof):
    if cof == "esp":
        return 0
    if cof == "lat":
        return data.MENU["latte"]["ingredients"]["milk"]
    if cof == "cap":
        return data.MENU["cappuccino"]["ingredients"]["milk"]

def cost_needed(cof):
    if cof == "esp":
        return data.MENU["espresso"]["cost"]
    if cof == "lat":
        return data.MENU["latte"]["cost"]
    if cof == "cap":
        return data.MENU["cappuccino"]["cost"]

def ask_for_money():
    q = int(input("Please insert quarters: "))
    d = int(input("Please insert dimes: "))
    n = int(input("Please insert nickles: "))
    p = int(input("Please insert pennies: "))
    return round(q*0.25+d*0.1+n*0.05+p*0.01, 2)


def coffeemach(water, milk, coffee, money):
    name = input("What is your name? ")
    choice = input(f"Good morning {name}. What would you like today? ").lower()
    choice = choice[:3]
    if choice != "esp" and choice != "lat" and choice != "cap" and choice != "rep":
        print("Not an option")
        coffeemach(water, milk, coffee, money)
    elif choice == "rep":
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
    else:
        print(f"You need ${cost_needed(choice)}")
        money_input = ask_for_money()
        if money_input < cost_needed(choice):
            print(f"Sorry, you do not have enough money. ${money_input} refunded.")
        else:
            water -= water_used(choice)
            milk -= milk_used(choice)
            coffee -= coffee_used(choice)
            if water < 0:
                print(f"Sorry, not enough water. ${money_input} refunded.")
                water += water_used(choice)
                coffee += coffee_used(choice)
                milk += milk_used(choice)
            elif coffee < 0:
                print(f"Sorry, not enough coffee. ${money_input} refunded.")
                coffee += coffee_used(choice)
                water += water_used(choice)
                milk += milk_used(choice)
            elif milk < 0:
                print(f"Sorry, not enough milk. ${money_input} refunded.")
                milk += milk_used(choice)
                coffee += coffee_used(choice)
                water += water_used(choice)
            else:
                money += cost_needed(choice)
                change = round(money_input - cost_needed(choice), 2)
                print(f"Enjoy your ☕. Your change is ${change}")
    power = input("Press enter to continue type 'off' to turn off: ")
    print("\n")
    if power == "off":
        return "off"
    else:
        coffeemach(water, milk, coffee, money)


