# Exercises For Dictionaries

## Exercise 1

1. Create a file named `birthdays.py` in this folder.
2. In that file create a dictionary with the following key-value pairs:
- key: dan, value: april 14th
- key: gary: value: june 23rd
- key: richard, value: february 2nd
- key: jessica, value: october 30th
- key: mary, value: december 25th
3. Prompt the user for a name, and then print out the birthday of that person.
If they are in the list then print out their birthday, otherwise print out "Sorry, we don't have NAMEHERE's birthday.". The output should look like the following:
- name in the dictionary
```
$ python birthdays.py
Who's birthday do you want to look up? dan
dan's birthday is april 14th
```
- name not in the dictionary
```
$ python birthdays.py
Who's birthday do you want to look up? Quince
Sorry, we don't have Quince's birthday.
```

## Exercise 2
1. Create a file named `pizza_prices.py` in this folder.
2. Create two dictionaries.
  - The first dictionary is named `toppings` with the following key-value pairs
    - key: cheese, value: True
    - key: pepperoni, value: True
    - key: mushrooms, value: False
    - key: pineapple, value: False
    - key: anchovies, value: True
    - key: olives, value: False
    - key: sausage, value: True
  - The second dictionary is the `toppings_prices` dictionary with the following key-value pairs
    - key: cheese, value: 0.5
    - key: pepperoni, value: 2.0
    - key: mushrooms, value: 1.0
    - key: pineapple, value: 0.5
    - key: anchovies, value: 1.5
    - key: olives, value: 1.25
    - key: sausage, value: 2.25
3. Calculate the price of the pizza based on the topping prices, add a 12$ base price and an 18% tip to the pizza. Print out the toppings of the pizza and the total price of the pizza. The output should look like the following:
```
$ python pizza_prices.py
The toppings of your pizza are:
cheese
pepperoni
No mushrooms
No pineapple
anchovies
No olives
sausage
Your total is: $21.535
```