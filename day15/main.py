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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def check_resources(drink: str):
    for key in MENU["cappuccino"]["ingredients"]:
        if resources[key] < MENU["cappuccino"]["ingredients"][key]:
            print(f"Sorry there is not enough {key}")
            return False
    return True


def make_coffee(drink: str):
    for key in MENU["cappuccino"]["ingredients"]:
        resources[key] = resources[key] - MENU["cappuccino"]["ingredients"][key]
    print(f"Here is your {drink}. Enjoy!")


status = True

while status:
    drink = input("What drink would you like (espresso/latte/cappuccino) ").lower()
    if drink == "off":
        status = False
    elif drink == "report":
        print(resources)
    else:
        if check_resources(drink):
            quarters, dimes, nickels, pennies = map(
                int,
                input(
                    "Enter coins: quarters, dimes, nickels, pennies like 1 1 0 1 for .36 "
                ).split(),
            )
            cost = MENU[drink]["cost"]
            amount = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
            if amount < cost:
                print("Sorry thats not enough money. Money refunded")
            elif amount > cost:
                print(f"Here is your change: {amount - cost}")
            resources["money"] = resources["money"] + cost  # type: ignore
            make_coffee(drink)
