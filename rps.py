# import random number
from random import randint

#create a list of computer choice options, list starts at 0. 0=Rock, 1=Paper...
choices = ["Rock", "Paper", "Scissors"]

#assign a random number that corresponds to one of the above choices
computerChoice = choices[randint(0,2)]

#set p[laying to true
playing = True

while playing == True:
#set player to True raw_input for 2.7 just input for later versions
    playerChoice = raw_input("Rock, Paper, Scissors? (Type 'q' to quit)\n")
    if playerChoice == "q":
        playing = False
    elif playerChoice == computerChoice:
        print("Tie!")
    elif playerChoice == "Rock":
        if computerChoice == "Paper":
            print("You lose! " + computerChoice + " covers " + playerChoice)
        else:
            print("You win! " + playerChoice + " smashes " + computerChoice)
    elif playerChoice == "Paper":
        if computerChoice == "Scissors":
            print("You lose! " + computerChoice + " cut " + playerChoice)
        else:
            print("You win! " + playerChoice + " covers " + computerChoice)
    elif playerChoice == "Scissors":
        if computerChoice == "Rock":
            print("You lose... " + computerChoice + " smashes " + playerChoice)
        else:
            print("You win! " + playerChoice + " cuts " + computerChoice)
    else:
        print("That's not a valid play. Check your spelling!")


    computerChoice = choices[randint(0,2)]
