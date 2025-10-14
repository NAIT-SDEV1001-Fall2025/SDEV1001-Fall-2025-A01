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

#### LOGICAL OPERATORS ####

# Logical operators allow us to combined multiple conditions into a single if statement. They are placed between each condition that we are checking. This gives us more flexibility and gives us the ability to have more complex logic.

# There is no limit to the number of comparisons that can be combined with logical operators.

# and : All conditions must be true
# or  : At least one condition must be true
# not : Inverts the condition

age = int(input("Enter your age: "))
has_license = input("Do you have a license? ")

# in order for someone to drive, they must be at least 16 years old AND they must have a license
if age >= 16 and has_license == "yes":
    print("You can drive.")

has_parent = input("Do you have a parent with you? ")

# For someone to see an R-rated movie, they must be at least 18 OR accompanied by a parent
if age >= 18 or has_parent:
    print("You can see an R-rated movie")

# Placing the "not" operator in front of any comparison will invert the logical condition

if not age >= 18:
    print("You cannot go into a bar.")

#### IF-ELSE STATEMENTS ####

# An ELSE statement is a statement we can add to an if statement that will execute a block of code if the IF statement evaluates to False.

# ELSE statements do not require a comparison.

if age >= 18:
    print("You are an adult")
else:
    print("You are underage")

#### ELIF STATEMENTS ####

# ELIF statements (short for else-if) allows us to execute different blocks of code with different conditions.
# They are placed after an "if" statement, but before an "else" statement
# ELIF statements require comparisons

# In an "elif chain", the first statement that evaluates to True will execute and the rest will be skipped.

if age >= 18:
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
# 
# Incorrect indentation will result in an IndentationError and your code will not run. 