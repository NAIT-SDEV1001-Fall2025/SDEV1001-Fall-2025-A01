# LOOPING THROUGH DICTIONARIES
# Looping through dictionaries can be done in several ways: by key, by value, or by key/value pair.

# Here is a dictionary for us to work with:

grades = {
    "Prabhjot": 85,
    "Lin": 77,
    "Isaac": 90
}
# LOOPING OVER KEYS
# The default method of looping over keys is by key.

print("Students:")
for key in grades:
    print(f"- {key}")

# If we want to be explicit (more readable) that we are looping through keys, we can use the keys() method to show this.

print("Students:")
for student in grades.keys():
    print(f"- {student}")

# Both approaches will give us the same output, but using the keys() method makes our loops more readable by specifying what the key represents while still making it clear that we are looping through the dictionary's keys.


# LOOPING OVER VALUES
# To loop over the values in a dictionary, we can use the values() method.
# We can use this is some calculations if we wished. For example, finding the average grade of the students:

total = 0
for score in grades.values():
    total += score

average = total / len(grades)
print(f"Average score: {average}")

# LOOPING OVER KEY/VALUE PAIRS
# To loop over the keys and their values at the same time, we use the items() method.
for name, grade in grades.items():
    print(f"{name} scored {grade}")

# SORTING THE ITEMS BEFORE A LOOP
# Sometimes we may want to sort the output of a dictionary when looping through it. This can be useful for displaying results in a specific order, such as alphabetically by key.
# To do this, we use the sorted() function combined with the .items() method in our for loop.

inventory = {"oranges": 10, "apples": 5, "bananas": 15}
for fruit, count in sorted(inventory.items()):
    print(f"{fruit.title()}: {count}")