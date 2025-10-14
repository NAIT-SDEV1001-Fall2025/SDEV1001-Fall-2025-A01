def my_demo_function(number):
    print("Hello my friend!")
    print("You are inside my_demo_function()")
    print(f"You have entered the number {number} ")
    print("Leaving my_demo_function()")

user_input = int(input("Enter a number: "))

if user_input < 0:
    print("That number is negative.")
elif user_input < 10:
    print("That number is pretty small.")
elif user_input < 100:
    print("That number is a little bit bigger.")
else:
    print("That number is huge!")

print("Let's perform some math on that number")

user_input += 10000
user_input *= 3
user_input /= 5

my_demo_function(user_input)
my_demo_function(user_input * 2)
my_demo_function(user_input * 3)
my_demo_function(user_input * 4)

my_list = [5, 1, 30, 55, 11]

print(my_list)