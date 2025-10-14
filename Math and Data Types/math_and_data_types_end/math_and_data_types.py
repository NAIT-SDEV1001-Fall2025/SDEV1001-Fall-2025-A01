# Learning about Math
days_until_assignment_due = 14
print(f"Assignment due in {days_until_assignment_due} days")

# Subtraction Example
days_playing_squash = 2
print(f"Days spent playing squash: {days_playing_squash}")
# Reassign days_until_assignment_due to the result of the subtraction
days_until_assignment_due = days_until_assignment_due - days_playing_squash
print(f"Assignment due in {days_until_assignment_due} days")

# Addition Example
time_machine_days_added = 3
print(f"Days added by the time machine: {time_machine_days_added}")
# Reassign days_until_assignment_due to the result of the addition
days_until_assignment_due = days_until_assignment_due + time_machine_days_added
print(f"Assignment due in {days_until_assignment_due} days")

# Multiplication Example
time_warp_mutitplier = 2

# Reassign days_until_assignment_due to the result of the multiplication
print(f"Time warp multiplier: {time_warp_mutitplier}")
days_until_assignment_due = days_until_assignment_due * time_warp_mutitplier
print(f"Assignment due in {days_until_assignment_due} percieved days")

# Division Example
slowing_spell_divisor = 7
print(f"Instructor Typing slowing spell {slowing_spell_divisor} times")
# special_remainder_power and days_until_assignment_due variables
special_remainder_power = days_until_assignment_due % slowing_spell_divisor
days_until_assignment_due = days_until_assignment_due // slowing_spell_divisor

# Result of division
print("Result of the floor division using the slowing_spell_divisor: ")
print(days_until_assignment_due)
print("Remainder of the division using the slowing_spell_divisor: ")
print(special_remainder_power)

# Exponentiation Example

print("Special Remainder Power")
days_until_assignment_due = days_until_assignment_due ** special_remainder_power
print(f"Assignment due in {days_until_assignment_due} percieved days")

# Math Order of Operations
user_input_days = input("How many days until the newest assignment is due? ")

days_until_newest_assignment_due = int(user_input_days)
special_remainder_power = 2
# Reassign days_until_assignment_due to all of the operations we did above.
days_until_newest_assignment_due = (( days_until_newest_assignment_due -
                              days_playing_squash +
                              time_machine_days_added) * time_warp_mutitplier // slowing_spell_divisor
                              ) ** special_remainder_power

print("We did the same thing as before, but in one line: ")
print(f"Newest Assignment due in {days_until_newest_assignment_due} percieved days")
