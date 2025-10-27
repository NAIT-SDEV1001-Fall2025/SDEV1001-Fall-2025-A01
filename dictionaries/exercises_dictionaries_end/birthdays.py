birthdays = {
    "dan": "april 14th",
    "gary": "june 23rd",
    "richard": "february 2nd",
    "jessica": "october 30th",
    "mary": "december 25th",
}

name = input("Who's birthday do you want to look up? ")
if name in birthdays:
    print(f"{name}'s birthday is {birthdays[name]}")
else:
    print(f"Sorry, we don't have {name}'s birthday.")
