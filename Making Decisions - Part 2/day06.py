#### BASIC IF STATEMENT SYNTAX ####

# if <condition>:
#     <execute code>

# The condition is a statement that will evaluate to either True or False.
# If the condition is True, then the code inside the if "block" will execute.
# If the condition is False, then the if block will not execute.


# EXAMPLE:

userInput = input("Enter a number: ")

# comparisons need to be made between values of the same type, so we must convert this to an int
number = int(userInput)

#### COMPARISON OPERATORS ####
#
# The following are comparison operators, they appear between two values and will compare them.
# Comparison operators evaluate to either True or False

# == : Equal To
# != : Not Equal To
# >  : Greater Than
# <  : Less Than
# >= : Greater Than or Equal To
# <= : Less Than or Equal To

# The "==" operator checks to see if two values are exactly equal to each other
if number == 5:
    print("You entered 5")

# The "!=" operator checks if two values do not equal each other
if number != 5:
    print("You did not enter 5")

# The ">" operator checks to see if the value on the left is GREATER THAN the value on the right
if number > 5:
    print("You entered a number greater than 5")

# The "<" operator checks to see if the value on the left is LESS THAN the value on the right
if number < 5:
    print("You entered a number less than 5")

# The ">=" operator checks to see if the value on the left is GREATER THAN OR EQUAL TO the value on the right
if number >= 5:
    print("You entered a number greater than or equal to 5")

# The "<=" operator checks to see if the value on the left is LESS THAN OR QUAL TO the value on the right
if number <= 5:
    print("You entered a number less than or equal to 5")

### CONSTANTS ###
# Constants are a special type of variable that is never meant to change, like Pi or the speed of light. It is fixed throughout the entire program
# In python, the concept of a "constant" variable does not exist, so instead there is a specific naming convention used to indicate that a variable
# should be constant. Snake case, but all UPPER_CASE
# They are used just like regular variables

DRINKING_AGE = 18
DRIVING_AGE = 16

#### LOGICAL OPERATORS ####

# Logical operators allow us to combined multiple conditions into a single if statement. They are placed between each condition that we are checking. This gives us more flexibility and gives us the ability to have more complex logic.

# There is no limit to the number of comparisons that can be combined with logical operators.

# and : All conditions must be true
# or  : At least one condition must be true
# not : Inverts the condition

age = int(input("Enter your age: "))
has_license = input("Do you have a license? ")

# in order for someone to drive, they must be at least 16 years old AND they must have a license
if age >= DRIVING_AGE and has_license == "yes":
    print("You can drive.")

has_parent = input("Do you have a parent with you? ")

# For someone to see an R-rated movie, they must be at least 18 OR accompanied by a parent
if age >= DRINKING_AGE or has_parent == "yes":
    print("You can see an R-rated movie")

# Placing the "not" operator in front of any comparison will invert the logical condition

if not age >= DRINKING_AGE:
    print("You cannot go into a bar.")

#### IF-ELSE STATEMENTS ####

# An ELSE statement is a statement we can add to an if statement that will execute a block of code if the IF statement evaluates to False.

# ELSE statements do not require a comparison.

if age >= DRINKING_AGE:
    print("You are an adult")
else:
    print("You are underage")

#### ELIF STATEMENTS ####

# ELIF statements (short for else-if) allows us to execute different blocks of code with different conditions.
# They are placed after an "if" statement, but before an "else" statement
# ELIF statements require comparisons

# In an "elif chain", the first statement that evaluates to True will execute and the rest will be skipped.

if age >= DRINKING_AGE:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
elif age >= 4:
    print("You are a child")
else:
    print("You are a toddler")

#### INDENTATION ####
# In Python, indentation is very important. It is how python determines what blocks of code to execute and when.
# code that we want to execute inside of an if statement must be indented EXACTLY 4 SPACES

# Correct:
# if name == "Jared":
#     print("Hello Jared")
# 
# Incorrect:
# if name == "Jared":
#    print("Hello Jared")
# Incorrect:
# if name == "Jared":
#      print("Hello Jared")
# 
# Incorrect indentation will result in an IndentationError and your code will not run.

### MORE MATHEMATICAL OPERATORS

# In python, if we want to increment the value of a number variable, we can do so in two ways

myNum = 1

# Method 1:
myNum = myNum + 1

# Method 2:
myNum += 1

# With method 2, we combine the addition (+) and assignment (=) operators to increase the value of "myNum"
# The same can be done with all of the other mathematical operators, for example 

# multiplication:
myNum *= 2

# subtraction:
myNum -= 1

# division:
myNum /= 2

# exponents:
myNum **= 2

# integer division:
myNum //= 2

# modulus
myNum %= 2

### STRING FUNCTIONS ###
# Python has a lot of built in string functions that we can use to our advantage

myString = "   Hello Everyone!   "
print(myString)

# Use the upper() function to make the entire string upper case
print(myString.upper())

# Use the lower() function to make the entire string lower case
print(myString.lower())

# Use lstrip() to remove leading whitespace 
print(myString.lstrip())

# Use rstrip() to remove trailing whitespace 
print(myString.rstrip())

# Use strip() to remove both leading and trailing whitespace
print(myString.strip())

# Check if the string is a number (int or float), this is useful when validating user input
print(myString.isnumeric())

# and lastly, while not a string function itself, a very useful conditional is checking 