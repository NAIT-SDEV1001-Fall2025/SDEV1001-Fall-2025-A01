user_input = input("Enter a year: ")
year_guess = int(user_input)

if (year_guess % 4 == 0 and year_guess % 100 != 0) or (year_guess % 400 == 0):
    print(F"Is {year_guess} a leap year? true")
else: 
    print(F"Is {year_guess} a leap year? false")

