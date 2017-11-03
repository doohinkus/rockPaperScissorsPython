# import random number specifically integers
from random import randint

#create a list of computer choice options, list starts at 0. 0=Rock, 1=Paper...
choices = ["Rock", "Paper", "Scissors"]

#assign a random number that corresponds to one of the above choices
computerChoice = choices[randint(0,2)]

#set playing to true
playing = True

while playing == True:
#Use raw_input for 2.7 just input for later versions of python
    playerChoice = raw_input("Rock, Paper, Scissors? (Type 'q' to quit)\n")
    # if player chooses "q" break out the loop
    if playerChoice == "q":
        playing = False
    # computer and player make the same choice
    elif playerChoice == computerChoice:
        print("Tie!")
    # player choice is rock
    elif playerChoice == "Rock" and computerChoice == "Paper":
       print("You lose! " + computerChoice + " covers " + playerChoice)
    elif playerChoice == "Rock" and computerChoice == "Scissors":
        print("You win! " + playerChoice + " smashes " + computerChoice)

    # player choice is paper
    elif playerChoice == "Paper" and computerChoice == "Scissors":
        print("You lose! " + computerChoice + " covers " + playerChoice)
    elif playerChoice == "Paper" and computerChoice == "Rock":
        print("You win! " + playerChoice + " smashes " + computerChoice)

    # player choice is scissors
    elif playerChoice == "Scissors" and computerChoice == "Rock":
        print("You lose! " + computerChoice + " crushes " + playerChoice)
    elif playerChoice == "Scissors" and computerChoice == "Paper":
        print("You win! " + playerChoice + " cut " + computerChoice)
        
    # player entered something other than a valid choice
    else:
        print("That's not a valid play. Check your spelling!")

    # make another random choice for the computer
    computerChoice = choices[randint(0,2)]
