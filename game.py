from random import randint

t = ["stone","paper","scissor"]

computer = t[randint(0,2)]

player = False

while player == False:

    player = input("stone,paper,scissor? :")
    if player == computer:
        print("Tie")
    elif player == "stone":
        if computer == "paper":
            print("you lose",computer)
        else:
            print("you won",player)
    elif player == "paper":
        if computer == "scissor":
            print("you lose",player)
        else:
            print("you won",computer)
    elif player == "scissor":
        if computer == "stone":
            print("you lose",player)
        else:
            print("you won",computer)
    else:
        print("invalid")


