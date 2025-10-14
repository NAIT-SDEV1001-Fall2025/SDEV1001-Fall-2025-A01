# FOR vs FOREACH
# The loops we have been using are often known as foreach loops in other programming languages. In programming languages like C#, a for loop is structure in a way where we implement a variable that is used to count each iteration. That variable is often called 'i' and often used as the index for a list or array.
# Sometimes we require this functionality, but it is not directly available in python. To implement it in Python we make use of the range() function.

# RANGE FUNCTION
# range() takes two integerts, the starting number and the ending number, and create a sequences of integers that increment by 1 each time. We can then use this sequence, in our for loops to create a counting mechanism for lists.

# This will print the numbers 1-4
nums = range(1, 5)
for i in nums:
    print(i)

# If only one parameter is provided, then the first number will default to 0.
# This will print the numbers 0-4
nums = range(5)
for i in nums:
    print(i)

# range() by default increments by 1 step, but we can add a third parameter that will allow us to specify the steps. If we want to do this we must provide all three parameters, the first parameter cannot be omitted, even if we start at 0.

# The following will create a range that increments by 2 starting at 0
nums = range(0, 10, 2)

for i in nums:
    print(i)
# if we wanted to convert our sequence into a list that we can use, we can cast it as a list like this:

new_nums = list(nums)
# CALCULATING SQUARES
# This code will go through each number and print the squares

for i in nums:
    print(f"The square of {i} is {i ** 2}")

# USING RANGE() WITH FOR LOOPS
# the upper bound (second int) is not included in the result set. So this makes it very useful for iterating through a loop since we can avoid index out of range exceptions

# by passing the len(list) as a parameter to the range function, we are starting at 0, which is the first index, and ending at the length of the list -1, which is the last index.

# with this will loop through all of the animals:
animals = ["dog", "cat", "goose", "hamster"]
for i in range(len(animals)):
    print(f"A cool animal is: {animals[i]}")