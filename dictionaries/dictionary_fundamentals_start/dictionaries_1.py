####### DICTIONARIES #######
# Dictionaries are collections of data like lists. But instead of storing values based on an index, they are based on key/value pairs. If you have ever heard of or used JSON documents, they are basically dictionaries.
# A "Key" is a named string that is used by the dictionary to store the value. Similar to how physical dictionaries have the word and a definition. The "key" would be the word and the "value" would be the definition.
# All keys must be unique and should follow the same naming convention as variables.
# In python, values can be any data type.
# Dictionaries are useful for represented structured data like a game character or a product.
# In other programming languages, this data structure might be called a "map" or an "associative array"

# To create a new dictionary we use curly braces {}

# create an empty dictionary:

my_dictionary = {}

# We can initialize a dictionary with existing key / value pairs by using the ':' to separate the key and value.

student = {
    "name": "Gertrude",
    "age": 78,
    "major": "Artificial Intelligence",
    "grades": [90,70,100]
}

# Because the values can be anything, they can stored lists and even other dictionaries.

# To access the values in a dictionary, we need to make use of the key.

print(f"The student's name is {student["name"]}")

# To update the value in a dictionary, we make use of the key to access that value and then assign a new value to it.
# here we will increment the student's age.

student["age"] += 1

# To add a new key/value pair to the dictionary, we can follow the same structure as updating the value, except using the new key.

student["email"] = "lady_rude@aol.com"

# Now the student dictionary will have an entry called "email"

print(student)

# LOOPING THROUGH A DICTIONARY

# An easy way to loop through a dictionary is to use a for loop to iterate through all of the keys and then use the keys to access the values in the dictionary.

print("Here are the details of the student:")
for key in student:
    print(f"{key}: {student[key]}")

# Another way to loop through a dictionary is using the .items() method after the dictionary name. It will give us access to both the key and value that we can use in our loop:

print("Here are the details of the student again:")
for key, value in student.items():
    print(f"{key}: {value}")

# ACCESSING NON-EXISTENT KEYS

# If you try and access a key that doesn't exist in the dictionary, you will get a KeyError
# print(student["hobbies"])

# There are two primary ways to prevent a KeyError from occurring: using the get() method or checking if a key exists before accessing it.

# THE get() METHOD.
# The get() method is a way to return the value of the get, or if the key is missing, it will return a default value specified.

middle = student.get("middle_name", "N/A")
print(f"Middle Name: {middle}")

# If the middle_name key exists in the dictionary, then the value of the "middle" variable will contain the value of the middle_name key
# If the middle_name key does not exists, "middle" will have a value of "N/A"

# CHECKING FOR KEYS
# The other way to prevent a KeyError from occurring is by using "in" to check if the key exists at all.

if "email" in student:
    print(f"Email is: {student["email"]}")
else:
    print("No email on file.")

# NESTED DICTIONARIES
# Because the values of items in a dictionary can be anything, we can nest dictionaries inside other dictionaries to create more complex data structures.
# For example we could have a store inventory that has the stock of our items as well as details about each item:

inventory = {
    "apple": {"price": 1.0, "stock": 30},
    "banana": { "price": 2.0, "stock": 50}
}

# To access the values in the nested dictionaries, we need to add access both keys in square brackets directly after each other [][]
# For example, to get the number of apples in stock:

print(f"Stock: {inventory["apple"]["stock"]}")