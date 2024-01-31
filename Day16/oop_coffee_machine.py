from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
coinstar = MoneyMachine()

while True:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    while choice not in ['report', 'espresso', 'latte', 'cappuccino', 'off']:
        print("Invalid response. Please try again.")
        choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if choice == 'report':
        coffee_machine.report()
        coinstar.report()
    elif choice == 'off':
        break
    else:
        if coffee_machine.is_resource_sufficient(menu.find_drink(choice)) and coinstar.make_payment(menu.find_drink(choice).cost):
            coffee_machine.make_coffee(menu.find_drink(choice))