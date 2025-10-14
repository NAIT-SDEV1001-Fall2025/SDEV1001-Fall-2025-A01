print('''Welcome to the Ultimate Gym
Please select a membership package:
- Package A: $40/month, 4 months (short-term package)
- Package B: $55/month, 8 months (standard package)
- Package C: $75/month, 12 months (regular package)
- Package D: $100/month, 12 month (premium package, includes 4 free personal training sessions)
''')
package = input("Enter the package letter (A/B/C/D): ")

match package.upper():
    case "A":
        print("You have selected Package A")
        print("Your monthly fee is $40")
        print("Your total fee is $160")
    case "B":
        print("You have selected Package B")
        print("Your monthly fee is $55")
        print("Your total fee is $440")
    case "C":
        print("You have selected Package C")
        print("Your monthly fee is $75")
        print("Your total fee is $900")
    case "D":
        print("You have selected Package D")
        print("Your monthly fee is $100")
        print("Your total fee is $1200")
    case _:
        print("Invalid package selected")
        print("Please select a valid package")