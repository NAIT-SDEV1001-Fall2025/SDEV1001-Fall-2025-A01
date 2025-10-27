toppings = {
    "cheese": True,
    "pepperoni": True,
    "mushrooms": False,
    "pineapple": False,
    "anchovies": True,
    "olives": False,
    "sausage": True
}

toppings_prices = {
    "cheese": 0.5,
    "pepperoni": 2.0,
    "mushrooms": 1.0,
    "pineapple": 0.5,
    "anchovies": 1.5,
    "olives": 1.25,
    "sausage": 2.25
}

price = 12
for topping, add in toppings.items():
    if add:
        price += toppings_prices[topping]

price = price * 1.18

print("The toppings of your pizza are:")
for topping, add in toppings.items():
    if add:
        print(topping)
    else:
        print("No " + topping)

print("Your total is: $" + str(price))