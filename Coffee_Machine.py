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
    },
}

reserve = {
    "water": 100,
    "milk": 50,
    "coffee": 76,
    "money": 2.5,
}

def report():
    print(f"Water: {reserve['water']}")
    print(f"Milk: {reserve['milk']}")
    print(f"Coffee: {reserve['coffee']}")
    print(f"Money: {reserve['money']}")

def coins():
    """Ask user for payment in coints and add them up"""
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    total_coins = (
        (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    )
    return total_coins

def transaction(total_coins, total_bill):
    if total_coins < total_bill:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        change = total_coins - total_bill
        print(f"Here is ${round(change, 2)} in change.")
        print(f"Here is your {order} ☕. Enjoy!")
        return True

make_coffee = True
total_bill = 0

while make_coffee:
    order = input(
        "What would you like? (espresso, latte, or cappuccino?) ").lower()
    if order == "off":
        make_coffee = False
    elif order == "report":
        report()
    else:
        coffee = MENU[order]
        print("Please insert coins.")
        total_coins = coins()
        transaction(total_coins, total_bill)
        break

reserve['money'] += total_bill

