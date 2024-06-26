# Task 1

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
else:
    place == "Cave"
    print("You've found a hidden treasure")

# Task 2


place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("Climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    # else:
    #     print("Oops, wrong answer! Please run again.")
elif place == "cave":
    action = input("Light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("Nice! You encounter a 10-foot demon monster.")
    elif action == "proceed in the dark":
        print("Good luck! They might not even see you ")
    # else:
    #     print("Oops, wrong answer! Please run again.")


# Task 3

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("Climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
        pass
elif place == "cave":
    action = input("Light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("Nice! You encounter a 10-foot demon baby.")
    elif action == "proceed in the dark":
        print("Good luck! They might not even see you, teehee ")
    else:
        pass



