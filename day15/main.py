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
}


def check_resources(drink: str):
    MENU["cappuccino"]


status = True

while status:
    drink = input("What drink would you like (espresso/latte/cappuccino) ").lower()
    if drink == "off":
        status = False
    elif drink == "report":
        print(resources)
    else:
        check_resources(drink)
