from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
menu = Menu()
moneyMachine = MoneyMachine()

while (True):
    user_choice = input(f"What would you like? {menu.get_items()} ").lower()

    if user_choice == "off":
        print("Goodbye! ")
        break
    elif user_choice == "report":
        coffee_machine.report()
        moneyMachine.report()
    elif (user_choice == "espresso") or (user_choice == "latte") or (user_choice == "cappuccino"):
        if(coffee_machine.is_resource_sufficient(menu.find_drink(user_choice))) and (moneyMachine.make_payment(menu.find_drink(user_choice).cost)):
            coffee_machine.make_coffee(menu.find_drink(user_choice))