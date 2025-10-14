# The match-case statement is used to match a variable against a list of patterns. It is more
# readable than a long set of if/elif statements
# When checking many possible values, it is much easier to maintain.
# The wildcard "_" should always be used as the default for when there are unmatched cases.

# It follows the syntax:
# match <variable>:
#     case <pattern1>:
#         <code to execute>
#     case <pattern2>:
#         <code to execute>
#     case <pattern3>:
#         <code to execute>
#     case _:
#         <default code>

value = input("Enter the name of a fruit: ").lower()

match value:
    case "apple":
        print("A nice crunchy apple.")
    case "banana":
        print("Bananarama!")
    case _:
        print("I don't know that fruit...")

# You can match multiple values in a single case statement by using the pipe | between the values, similar to an OR

day_of_week = input("Which day of the week is it?").lower()

match day_of_week:
    case "monday":
        print("It's monday....")
    case "thursday":
        print("Nearly there!")
    case "saturday" | "sunday":
        print("Weekend!")
    case _:
        print("Just another day...")