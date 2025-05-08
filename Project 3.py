# Guess the Number - You try to guess the number

import random

print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 100.")

secret_number = random.randint(1, 100)
guess = 0
attempts = 0

while guess != secret_number:
    guess = int(input("Take a guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed it in", attempts, "tries.")
