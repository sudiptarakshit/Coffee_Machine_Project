# TODO: 2. Check resources are sufficient to make drink order.

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
    }
}
profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredient):
    """Returns True when order can be made, Fasle if ingredients are insufficient."""
    is_enough = True
    for item in order_ingredient:
        if order_ingredient[item]>= resources[item]:
            print(f"Sorry there is not enough {item}")
            is_enough = False
    return is_enough # this will exit the function


def process_coins():
    """Returns the total calculated from the coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quartes?: "))*0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True if payment is accepted, or False if the money is insufficient."""
    if money_received>= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")



# TODO: 1. Print report of all coffee machine resources

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")

    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
        print(f"Water: {resources['water']}ml")

    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(money_received=payment,drink_cost=drink["cost"]):
                make_coffee(drink_name=choice, order_ingredients=drink["ingredients"])








