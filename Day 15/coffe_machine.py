from code import MENU, resources
flag = True
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01
profit = 0



def coin_total():
    total = 0
    coins = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01}
    for key in coins:
        ask_coin = float(input(f"Please insert {key} coin: "))
        some_name = ask_coin * coins[key]
        total += some_name
    return total


def report_check(coffe_type):
    if resources["water"] < MENU[coffe_type]["ingredients"]["water"]:
        print(f"Sorry there is not enough {resources['water']}ml water.")
        return False
    if coffe_type != "espresso" and resources["milk"] < MENU[coffe_type]["ingredients"]["milk"]:
        print(f"Sorry there is not enough {resources['milk']}ml  milk.")
    if resources["coffee"] < MENU[coffe_type]["ingredients"]["coffee"]:
        print(f"Sorry there is not enough {resources['coffee']} coffee.")
    return True


def report_deduce(user_input):
    if user_input == "espresso":
        resources["water"] -= MENU[user_input]["ingredients"]["water"]
        resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]
    else:
        resources["water"] -= MENU[user_input]["ingredients"]["water"]
        resources["milk"] -= MENU[user_input]["ingredients"]["milk"]
        resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]

        



def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    profit = resources["cost"]

    print(f"water : {water}")
    print(f"milk : {milk}")
    print(f"coffee {coffee}")
    print(f"cost {profit}")



def coffe_machine(user_input):
    if report_check(user_input):
        total_value = coin_total()
        # print(total_value)
        # print(MENU[user_input]["cost"])
        if total_value < MENU[user_input]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            flag = False
            return False
        
        elif total_value >= MENU[user_input]["cost"]:
            resources["cost"] += MENU[user_input]["cost"]
            change = total_value - MENU[user_input]["cost"] 
            if change:
                print(f"""Here is ${round(change,2)} dollars in change.""")
                return True
            return True
    elif user_input == "off":
        flag = False
        return False
    return False

while(flag):

    user_input = input(
        """What would you like? (espresso/latte/cappuccino): """).lower()

    if user_input != "report" and coffe_machine(user_input) :
        report_deduce(user_input)
        report()
        print("Here is your latte ☕️. Enjoy!")
        
    elif user_input == "report":
        report()
        flag = False
    else:
        flag = False
