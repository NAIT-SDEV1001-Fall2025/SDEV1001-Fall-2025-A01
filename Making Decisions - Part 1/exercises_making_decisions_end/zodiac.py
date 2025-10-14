year = input("Enter a year: ")
year_guess = int(year)

cycle_number = year_guess % 12

if cycle_number == 0:
    print("monkey")
elif cycle_number == 1:
    print("rooster")
elif cycle_number == 2:
    print("dog")
elif cycle_number == 3:
    print("pig")
elif cycle_number == 4:
    print("rat")
elif cycle_number == 5:
    print("ox") 
elif cycle_number == 6:
    print("tiger")
elif cycle_number == 7:
    print("rabbit")
elif cycle_number == 8:
    print("dragon")
elif cycle_number == 9:
    print("snake")
elif cycle_number == 10:
    print("horse")
elif cycle_number == 11:
    print("sheep")
else:
    print("error")