menu = {
    "dishes": [
        {"name": "Karbonara", "price": 240},
        {"name": "Pizza", "price": 300},
        {"name": "Pasta", "price": 200},
        {"name": "Salamy white", "price": 500},
    ],

    "drinks": [
        {"name": "Wine", "price": 40},
        {"name": "Cola", "price": 30},
        {"name": "7up", "price": 45},
        {"name": "Fanta", "price": 50},
    ],
}

waitress = [
    {
        "name": "Julia",
        "tips": "10%"
    },

    {
        "name": "Aida",
        "tips": "12%"
    },

    {
        "name": "transSam",
        "tips": "14%"
    },

    {
        "name": "Gaga",
        "tips": "24%"
    },
]

user = input("Hello! What's your name? ")


def greeting(array, user):
    print("*******************************************")
    print("Hello,", user, "!")
    n = 0
    while n < len(array):
        print('\033[1m' + array[n]["name"] + '\033[0m')
        n = n + 1
    print("are glad to see you!")
    print("*******************************************")


def choose_a_waitress(array):
    print("*******************************************")
    print("You will need to choose your waitress.")
    print("Our waitresses:")
    print("*******************************************")
    n = 0
    while n < len(array):
        print('\033[1m' + str(n + 1) + ". " + array[n]["name"] + '\033[0m')
        n = n + 1
    print("*******************************************")
    choice = input("1, 2, 3, or 4: ")
    if choice != "1" and choice != "2" and choice != "3" and choice != "4":
        print("Wrong choice, buddy")
        choose_a_waitress(array)
    else:
        tip = int(array[int(choice) - 1]["tips"][:2])
        print("All right. Expect a tip of", tip, "percent")
        print("*******************************************")
        return tip


def menu_display():
    print("Here is our menu.")
    print("*******************************************")
    print("We have the following dishes: ")
    n = 0
    while n < len(menu["dishes"]):
        print('\033[1m' + menu["dishes"][n]["name"] + " - $" + str(menu["dishes"][n]["price"]) + '\033[0m')
        n = n + 1
    print("*******************************************")
    print("We also have the following drinks: ")
    n = 0
    while n < len(menu["drinks"]):
        print('\033[1m' + menu["drinks"][n]["name"] + " - $" + str(menu["drinks"][n]["price"]) + '\033[0m')
        n = n + 1


def to_eat_or_not_to_eat():
    decision = input("You can see our menu or go away. M for Menu or Q to quit: ")
    decision = decision.lower()
    if decision == "q":
        final_decision = input("Are you sure you want to quit? Y or N: ")
        final_decision = final_decision.lower()
        if final_decision == "y":
            print("Have a nice day!")
            ultimate_decision = False
        if final_decision == "n":
            ultimate_decision = True
            menu_display()
    elif decision != "q" and decision != "m":
        print("Wrong choice, buddy")
        ultimate_decision = False
    elif decision == "m":
        ultimate_decision = True
        menu_display()
    return ultimate_decision


def price_count(initial_amount, money):
    global tip
    is_running = True
    while is_running == True:
        waitress_request = input("What dish or drink do you want to order? Or press q to exit ")
        if waitress_request == "q":
            print("We hope you enjoyed your meal. Your bill is $", initial_amount - money)
            is_running = False
        else:
            n = 0
            while n < len(menu["dishes"]):
                if waitress_request in menu["dishes"][n]["name"]:
                    price = menu["dishes"][n]["price"] + (menu["dishes"][n]["price"] * tip / 100)
                    money = money - price
                    if money < 0:
                        print("You've run out of money!")
                        print("Please pay the bill and have a nice day!")
                        is_running = False
                elif waitress_request in menu["drinks"][n]["name"]:
                    price = menu["drinks"][n]["price"] + (menu["drinks"][n]["price"] * tip / 100)
                    money = money - price
                    if money < 0:
                        print("You've run out of money!")
                        print("Please pay the bill and have a nice day!")
                        is_running = False
                n = n + 1
            if money > 0 and waitress_request != "q":
                price_count(initial_amount, money)
            return money


greeting(waitress, user)
ultimate_decision = to_eat_or_not_to_eat()
if ultimate_decision == True:
    tip = choose_a_waitress(waitress)
    price_count(500, 500)
elif ultimate_decision == False:
    pass
