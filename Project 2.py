# Guess the Number - Computer guesses your number

import random

print("Think of a number between 1 and 100, and I'll try to guess it!")
input("Press Enter when you're ready...")

low = 1
high = 100
tries = 0

while True:
    guess = random.randint(low, high)
    print("Is your number", guess, "?")
    answer = input("Type 'h' if it's too high, 'l' if it's too low, or 'c' if it's correct: ")

    tries += 1

    if answer == 'h':
        high = guess - 1
    elif answer == 'l':
        low = guess + 1
    elif answer == 'c':
        print("Yay! I guessed your number in", tries, "tries.")
        break
    else:
        print("Please enter only 'h', 'l', or 'c'.")
