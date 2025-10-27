# burger dictionary
burger = {
    'patties': 1,
    'patty_type': 'beef',
    'cheese': True,
    'toppings': ['lettuce', 'tomato', 'onion', 'pickles', 'ketchup', 'mustard'],
    'bun': 'sesame seed'
}
# changing the values in the dictionary
burger['patties'] = 2
burger['patty_type'] = 'vegetarian'
burger['cheese'] = False
burger['bun'] = 'whole wheat'

print("Here's what's in your burger:")
print(f"{burger['patties']} {burger['patty_type']} patties is on your burger.")

print(f"Your burger has {burger['bun']} bun.")
if burger['cheese']:
    print("Cheese is on your burger.")
else:
    print("No cheese on your burger.")

print("here's a list of toppings.")
for topping in burger['toppings']:
    print(f"- {topping}")

# with a value that doesn't exist.
burger['gluten_allergy'] = True

gluten_allergy = burger.get('gluten_allergy', False)
if gluten_allergy:
    print("we have removed the gluten from the burger")

