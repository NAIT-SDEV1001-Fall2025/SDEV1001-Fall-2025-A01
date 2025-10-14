concert_name = input("What is the name of the concert tonight? ")
has_ticket = input("Do you have a ticket? (y/n) ")

if concert_name == "taylor swift" and has_ticket == "y":
    print("you're in the right place")
    print("have fun!")
elif concert_name == "taylor swift" and has_ticket == "n":
    print("sorry you need a ticket to get in")
elif concert_name == "billie eilish":
    print("this concert is next door")
else:
    print("this is not the concert you are looking for")


