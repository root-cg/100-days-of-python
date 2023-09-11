from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



my_report = CoffeeMaker()
ask_menu = Menu()
ask_coin = MoneyMachine()

is_on = True

while(is_on):
    options = ask_menu.get_items()
    ask_user = input("What would you like? ({options}): ")
    if ask_user == "off":
        is_on = False
    elif ask_user == "report":
        my_report.report()
        ask_coin.report()
    else:
        drink =ask_menu.find_drink(ask_user)
        if my_report.is_resource_sufficient(drink) and ask_coin.make_payment(drink.cost):
                my_report.make_coffee(drink)
