# Rock, Paper, Scissors Game

import random

print("Let's play Rock, Paper, Scissors!")
options = ["rock", "paper", "scissors"]

user = input("Choose rock, paper, or scissors: ").lower()
computer = random.choice(options)

print("Computer chose:", computer)

if user == computer:
    print("It's a tie!")
elif user == "rock":
    if computer == "scissors":
        print("You win!")
    else:
        print("You lose.")
elif user == "paper":
    if computer == "rock":
        print("You win!")
    else:
        print("You lose.")
elif user == "scissors":
    if computer == "paper":
        print("You win!")
    else:
        print("You lose.")
else:
    print("Invalid input.")
