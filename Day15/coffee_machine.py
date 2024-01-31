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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resouces(drink, machine_resources):
    """Checks if the coffee machine has the necessary resources need to the make the drink. Returns True if it does and False otherwise."""
    if drink['ingredients']['water'] > machine_resources['water']:
        print("Sorry there is not enough water.")
        return False
    elif drink.get('ingredients').get('milk', 0) > machine_resources['milk']:
        print("Sorry there is not enough milk.")
        return False
    elif drink['ingredients']['coffee'] > machine_resources['coffee']:
        print("Sorry there is not enough coffee.")
        return False
    
    return True

def check_money(drink, quarters, dimes, nickels, pennies, machine_coins):
    """Checks if amount collected is >= amount needed. Returns True and adds coins to coffee machine resources, returns False otherwise."""
    amount_needed = drink['cost']
    if amount_needed == 1.5:
        beverage = 'espresso'
    elif amount_needed == 2.5:
        beverage = 'latte'
    elif amount_needed == 3.0:
        beverage = 'cappuccino'
    total_collected = quarters + dimes + nickels + pennies
    if amount_needed > total_collected:
        print("Sorry that's not enough money. Money refunded.")
        return False
    machine_coins += amount_needed
    print(f"Here is ${round(total_collected - amount_needed, 2)} in change.")
    print(f"Here is your {beverage} ☕ Enjoy!")
    return True

def deduct_resources(machine_resources, water, milk, coffee):
    """Deduct the machine resources if the transaction was successful."""
    machine_resources['water'] = machine_resources['water'] - water
    machine_resources['milk'] = machine_resources['milk'] - milk
    machine_resources['coffee'] = machine_resources['coffee'] - coffee

def transaction(drink, coins):
    """Collects the money and completes the transaction if successful."""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    if check_money(drink, quarters, dimes, nickels, pennies, coins):
        deduct_resources(resources, drink['ingredients']['water'], drink['ingredients'].get('milk', 0), drink['ingredients']['coffee'])

while True:
    request = input("What would you like? (espresso/latte/cappuccino): ").lower()
    while request not in ['report', 'espresso', 'latte', 'cappuccino', 'off']:
        print("Invalid response. Please try again.")
        request = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if request == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources.get('money', 0.0)}")
    elif request == 'off':
        break
    elif (request == 'espresso') and check_resouces(MENU[request], resources):
        transaction(MENU[request], resources.get('money', 0.0))
    elif (request == 'latte') and check_resouces(MENU[request], resources):
        transaction(MENU[request], resources.get('money', 0.0))
    elif (request == 'cappuccino') and check_resouces(MENU[request], resources):
        transaction(MENU[request], resources.get('money', 0.0))