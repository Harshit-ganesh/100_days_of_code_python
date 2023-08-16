#just a test
import math

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

cost = 0
flag = True
coffee = ["espresso", "latte", "cappuccino"]
things = ["milk", "water", "coffee"]


def cook(MENU, resources, entry):
    for key in resources:
        if entry == "espresso":
            if key == "milk":
                continue
        if resources[key] < MENU[entry]["ingredients"][key]:
            return key
        resources[key] = resources[key] - MENU[entry]["ingredients"][key]


while flag:
    entry = input("What would you like? (espresso/latte/cappuccino): ")
    if entry == "off":
        break
    elif entry == "report":
        for x, y in resources.items():
            print(f"{x.title()}: {str(y)}")
        print(f"Money :${cost}")
        continue
    elif not entry in coffee:
        print("""Sorry, Wrong Input.
        Please, Enter again.""")
        continue

    goods = cook(MENU, resources, entry)
    if goods in things:
        print(f"Sorry there is not enough {cook(MENU, resources, entry)}")

    print("Please insert coins.")
    quad = float(input("how many quarters?:"))
    dim = float(input("how many dimes?:"))
    nick = float(input("how many nickles?:"))
    penn = float(input("how many pennies?:"))
    paid = 0.25 * quad + 0.1 * dim + 0.05 * nick + 0.01 * penn
    to_pay = MENU[entry]["cost"]
    if to_pay > paid:
        print("Sorry that's not enough money. Money refunded.")
        continue
    else:
        cook(MENU, resources, entry)
        change = math.ceil(float(paid - to_pay))
        print(f"Here is ${change} in change.")
        cost = to_pay
        print(f"Here is your {entry} ☕.Enjoy!")
