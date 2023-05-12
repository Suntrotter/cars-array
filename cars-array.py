auto = [
    {"manufacturer": "VW",
     "price": "800"},
    {"manufacturer": "BMW",
     "price": "1500"},
    {"manufacturer": "MB",
     "price": "2500"},
    {"manufacturer": "FORD",
     "price": "2800"},
    {"manufacturer": "MERCEDES",
     "price": "3800"},
    ]

def append_info():
    model = input("Please enter the car model: ")
    price = input("Please enter the car price: ")
    auto.append({"manufacturer": model, "price": price})
    print("The information has been sucessfully added!")
    print(auto)
    add_more = input("Do you want to add more? Y or N: ")
    add_more = add_more.lower()
    if add_more == "n":
        print("Bye then!")
    elif add_more == "y":
        append_info()
    else:
        print("You've typed something strange!")
    return auto
append_info()

def car_offer():
    print('\033[1m' + "We have the following cars to sell: ")
    n = 0
    while n < len(auto):
        print('\033[0m' + "We have a", auto[n]['manufacturer'], "that costs", auto[n]['price'], "US dollars")
        n = n + 1
car_offer()

def car_removal():
    model = input("Please enter the model of the car you want to remove: ")
    model = model.upper()
    if not any(d['manufacturer'] == model for d in auto):
        print("You've typed something strange!")
        car_removal()
    else:
        new_auto = [i for i in auto if not (i['manufacturer'] == model)]
        print("You've successfully removed the car!")
        print("Here is the new array: ", new_auto)
    return new_auto
car_removal()

def expensive_cars():
    n = 0
    expensive_cars = []
    while n < len(auto):
        if int(auto[n]['price']) >= 1800:
            expensive_cars.append({"manufacturer": auto[n]['manufacturer'], "price": auto[n]['price']})
        n = n + 1
    return expensive_cars
print("Here are our most expensive cars: ", expensive_cars())