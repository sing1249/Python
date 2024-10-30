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

#Asking user what would they want?

#


def collecting_money():
    print("Please enter coins:")
    quarters = int(input("How many quarters?:"))
    dimes = int(input("How many dimes?:"))
    nickles = int(input("How many nickles?:"))
    pennies = int(input("How many pennies?:"))
    dollars = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies* 0.01
    return dollars




MONEY = float(0.00)

def coffee_function(choice):
    global MONEY
    cost = MENU[choice]["cost"]
    money_given = collecting_money()
    if money_given >= cost:
            change = money_given - cost
            MONEY += cost
            print(f"Here is your change {change}")
            print(f"Here is your {choice}")
    else:
        print("Not enough money!")


def print_report():
    for a in resources:
        print(f"{a}: {resources[a]}ml" )
    print(f"Money: ${MONEY}")

def resource_depletion(choice):
    for a in MENU[choice]["ingredients"]:
        if a in resources:
            resources[a] -= MENU[choice]["ingredients"][a]


def check_resources(ingredients):
    for a in ingredients:
        if ingredients[a] >= resources[a]:
            print(f"Sorry there is not enough {a}")
            return False
    return True





coffee_want = True
while coffee_want:
    user_coffee = input("What would you like? (espresso/latte/cappuccino:)")

    if user_coffee == "espresso" or user_coffee == "latte" or user_coffee == "cappuccino":
        drink = MENU[user_coffee]
        if check_resources(drink["ingredients"]):
            coffee_function(user_coffee)
            resource_depletion(user_coffee)
    elif user_coffee == "report":
        print_report()
    elif user_coffee == "off":
        coffee_want = False










