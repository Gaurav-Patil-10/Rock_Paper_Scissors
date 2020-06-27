import random


def check(name):
    with open("rating.txt", 'r') as f:
        content = f.readlines()
        for x in content:
            x.rstrip("\n")
            my_list = x.split(" ")
            if name in my_list:
                return int(my_list[1])
                break
            else:
                return 0


def plays_default(play, comp):
    global k, rating
    if play == "!exit":
        k = False
    elif play == "scissors" and comp == "rock":
        print("Sorry, but computer chose rock")

    elif play == "rock" and comp == "paper":
        print("Sorry, but computer chose paper")

    elif play == "paper" and comp == "scissors":
        print("Sorry, but computer chose scissors")

    elif play == comp:
        print(f"There is a draw ({play})")
        rating += 50

    elif play == "scissors" and comp == "paper":
        print("Well done. Computer chose paper and failed")
        rating += 100

    elif play == "rock" and comp == "scissors":
        print("Well done. Computer chose scissors and failed")
        rating += 100

    elif play == "paper" and comp == "rock":
        print("Well done. Computer chose rock and failed")
        rating += 100
    elif play == "!rating":
        print(f"Your rating: {rating}")
    else:
        print("Invalid Input")


def plays_random(play, comp, list1):
    global rating, k
    if play == "!rating":
        print(f"Your rating: {rating}")
    elif play == "!exit":
        k = False
    elif play not in list1:
        print("Invalid Input")
    else:
        x = list1.index(play)
        losing = []
        losing.extend(list1[x+1:])
        wining = list1[:x]
        if play == comp:
            print(f"There is a draw ({play})")
            rating += 50
        elif comp in losing:
            print(f"Well done. Computer chose {comp} and failed")
            rating += 100
        elif comp in wining:
            print(f"Sorry, but computer chose {comp}")
            rating += 100


k = True
name = input("Enter your name: ")
print(f"Hello, {name}")
rating = check(name)
list_games = []
names_plays = input().split(",")
if len(names_plays) <= 2:
    list_games = ["rock", "paper", "scissors"]
else:
    list_games = names_plays

print("Okay, let's start")
while k:
    play = input("Enter your Options : !rating for rating and !exit for exiting :  ")
    comp = random.choice(list_games)

    if len(names_plays) <= 2:
        plays = plays_default(play, comp)
    else:
        plays = plays_random(play, comp, list_games)


print("Bye!")
