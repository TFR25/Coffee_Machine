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
    "money": 0,  # Add money to the reserve
}

def report():
    print(f"Water: {reserve['water']}")
    print(f"Milk: {reserve['milk']}")
    print(f"Coffee: {reserve['coffee']}")
    print(f"Money: ${reserve['money']:.2f}")

def coins():
    """Ask the user for payment in coins and add them up"""
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total_coins = (
        (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    )
    return total_coins

def transaction(total_coins, total_bill):
    if total_coins < total_bill:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        change = total_coins - total_bill
        reserve['money'] += total_bill  # Update the money in the reserve
        print(f"Here is ${round(change, 2)} in change.")
        return True

def pour_coffee(order_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        reserve[item] -= order_ingredients[item]
    print(f"Here is your {order_name} ☕️. Enjoy!")

make_coffee = True
total_bill = 0

while make_coffee:
    order = input("What would you like? (espresso, latte, or cappuccino?) ").lower()
    if order == "off":
        make_coffee = False
    elif order == "report":
        report()
    else:
        coffee = MENU[order]
        print("Please insert coins.")
        total_coins = coins()
        total_bill = coffee["cost"]
        if transaction(total_coins, total_bill):
            pour_coffee(order, coffee["ingredients"])

