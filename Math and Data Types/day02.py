# A data type is the type of information that is held inside of a variable.
# Strings, Integers, Floating Point Numbers, and Booleans are all different data types.

# A string is just basic text, wrapped in a "" or a ''

string1 = "This is string 1"
string2 = 'This is string 2'

# An integer is a positive or negative whole number
int1 = 45
int2 = -60000

# A float (floating point number) is a positive or negative decimal number
float1 = 66.6666
float2 = -424.511

# A Boolean has only two values: True or False. This data type is used for logical operations
bool1 = True
bool2 = False 

#CASTING
# Sometimes we may need to convert one variable type to another, this is a process known as "casting". You "cast" a variable to a different type.

# For example, we can convert the string "33" to the integer 33 using the int() function
string_to_int = int("45")

# We put the variable stringNumber inside of the parentheses of the int() function. The int() function will take that value and convert it to an integer.
# Once the variable is an integer we can perform mathematical operations with it.

# the same can be done with the float() function. We can convert a string (or an int) to a float.
string_to_float = float("3.14159")

# Same as with the int() function, we pass the string variable into the float() function, and the string will be converted into a float

# If we want to convert another variable to a string, we would use the str() function

float_to_string = str(float1)
int_to_string = str(int1)

# Not all variables can be cast safely. For example, we can cast the string "1" to an int or a float, but we cannot cast "hello" to an int or a float. If we do we will get a runtime error:

string_to_int = int("Hello")

# Python is a dynamically typed language, meaning that the data type of a variable can change. The data type of the variable is determined at runtime (when the program actually runs)

# To declare a variable as an integer, we assign it an integer value:

int_var = 5

# To declare a variable as a float, we assign it a float value (include the .0):

float_var = 5.0

# With dynamically typed languages, variables can change the data type. All we need to do is assign it a different value:

int_var = "Hello. Now I am a string."

# Be careful when doing this however, since changing the type of a variable could have unforeseen consequences in other parts of the code. It is better to keep the data types of a variable consistent.