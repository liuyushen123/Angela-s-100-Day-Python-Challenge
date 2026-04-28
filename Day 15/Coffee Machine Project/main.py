from data import MENU
from data import resources

#coffee_type = ("​What would you like? (espresso/latte/cappuccino): ")
def promt_report(key):
    key = key.lower()
    return resources[key]

def validation(coffee_type):
    #TODO check how much resources this coffee type needs
    #TODO check if we have enough resources
    for key in resources:
        if (key == "money"):
            continue
        elif (resources[key] < MENU[coffee_type]["ingredients"][key]):
            print(f"Sorry there is not enough {key}")
            return False
    return True
def make_coffee(currrent_resources, resources_needed):
    for i in currrent_resources:
        if i == "money":
            continue
        currrent_resources[i] -= MENU[resources_needed]['ingredients'][i]
    return currrent_resources
def process_payment(type_coffee):
    while True:
        try:
            quarters_amount = int(input("How many quarters?: "))
            dimes_amount =  int(input("How many dimes: "))
            nickles_amount = int(input("How many nickles?: "))
            pennies_amount = int(input("How many pennies?: "))
            break
        except ValueError:
            print("Sorry that is not the valid input")

    total_money = (quarters_amount * 0.25) + (dimes_amount * 0.10) + (nickles_amount * 0.05) + (pennies_amount * 0.01)

    if (total_money >= MENU[type_coffee]["cost"]):
        print(f"Here is ${total_money - MENU[type_coffee]["cost"]:.2f} is change")
        print(f"Here is your {type_coffee} enjoy!")
        resources['money'] += MENU[type_coffee]["cost"]

    else:
        print("Sorry that is not enough money. Money refunded")

def refill(resource_type,resource_amount,current_resource):
    try:
        resource_amount = int(resource_amount)
    except ValueError:
        print("Please choose the right amount")

    try:
        current_resource[resource_type] += resource_amount
    except KeyError:
        print("Please choose the right ingredient")
    
    return current_resource

def display_coffee():
    for item in MENU:
        print(f"{item:<12} ${MENU[item]['cost']}:")
        print(f"\tWater: {MENU[item]['ingredients']['water']}ml")
        print(f"\tMilk:{MENU[item]['ingredients']['milk']}ml")
        print(f"\tCoffee:{MENU[item]['ingredients']['coffee']}g")
        print()



while (True):
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if (user_choice == "off"):
        break
    
    elif (user_choice == "report"):
        print("Current resources:")
        print(f"\tWater: {promt_report("water")}ml")
        print(f"\tMilk: {promt_report("MiLk")}ml")
        print(f"\tCoffee: {promt_report("coffee")}g")
        print(f"\tMoney: ${promt_report("money")}")
    
    elif (user_choice == "espresso") or (user_choice == "latte") or (user_choice == "cappuccino"):
        if(validation(user_choice)):
            process_payment(user_choice)
            resources = make_coffee(resources,user_choice)
    elif (user_choice == "refill"):
        refill(input("What type of resource would you like to refill? (\"Water\", \"Milk\", \"Coffee\")"),input("How much would you like to refill?: "), resources)
    elif (user_choice == "display"):
        display_coffee()

    else:
        print("Sorry that is not a valid input")
