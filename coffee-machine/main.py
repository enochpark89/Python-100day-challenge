# Given References

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
    "money": 0,
}

COFFEE_MACHINE_POWER = 'on'


# Check resources

def check_resource(item_name):
    resource_ready = True
    if ITEM_SELECTED == 'espresso':
        ingredients_list = MENU[ITEM_SELECTED]['ingredients']
        for key, value in ingredients_list.items():
            if resources[key] < value:
                print(f"Sorry there is not enough {key}")
                resource_ready = False
    elif ITEM_SELECTED == 'latte':
        ingredients_list = MENU[ITEM_SELECTED]['ingredients']
        for key, value in ingredients_list.items():
            if resources[key] < value:
                print(f"Sorry there is not enough {key}")
                resource_ready = False
    else:
        ingredients_list = MENU['latte']['ingredients']
        for key, value in ingredients_list.items():
            if resources[key] < value:
                print(f"Sorry there is not enough {key}")
                resource_ready = False
    return resource_ready

def check_amount(total_inserted):
    enough_money = True
    item_cost = MENU[ITEM_SELECTED]['cost']
    if item_cost > total_inserted:
        print("Sorry that's not enough money. Money refunded.")
        enough_money = False
    elif item_cost < total_inserted:
        resources['money'] += item_cost
        change = total_inserted - item_cost
        rounded_change = round(change, 2)
        print(f"You gave too much ${rounded_change}")
    else:
        print("You gave the exact amount!")
        resources['money'] += item_cost
    return enough_money

while COFFEE_MACHINE_POWER == "on":
    # Create a menu for users to choose from
    print("========CHOOSE YOUR OPTION FROM BELOW=========")
    print("1. Order a coffee")
    print("2. Create a report of a current resource")
    print("3. Turn off a coffee mach1ine")

    user_option = input("Choice: ")

    # Create a switch_case function
    if user_option == "1":
        # If they choose 1, the ordering process starts.
        ITEM_SELECTED = input("What would you like? (espresso/latte/cappuccino):")

        # Check whether the resources are sufficient
        print("============Checking the resources===============")
        returned_resource_check = check_resource(ITEM_SELECTED)
        if not returned_resource_check:
            break
        print("We have enough resources to make that! :)")
        print("=================================================")

        # Process coins
        print("Please insert coin")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))

        total_inserted = quarters * .25 + dimes * .10 + nickles * .05 + pennies * .01
        rounded_total_inserted = round(total_inserted, 2)
        print(f"Total: {rounded_total_inserted}")

        # Check Transaction
        returned_amount_check = check_amount(total_inserted)
        if not returned_amount_check:
            break

        # Make coffee
        ingredients_list = MENU[ITEM_SELECTED]['ingredients']
        for key, value in ingredients_list.items():
            resources[key] -= value
        print("========== Resources left ============")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
        print("======================================")

        print("Here is your latte. Enjoy!")

    elif user_option == "2":
        print("========== Resources in the machine ============")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
        print("================================================")
    elif user_option == "3":
        COFFEE_MACHINE_POWER = 'off'


