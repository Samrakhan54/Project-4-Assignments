# Hangman Game (Simple)

word = "python"
guessed = []
tries = 6

print("Welcome to Hangman!")

while tries > 0:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    print(display)

    if "_" not in display:
        print("You won!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("You already guessed that.")
        continue

    guessed.append(guess)

    if guess not in word:
        tries -= 1
        print("Wrong guess. Tries left:", tries)

if tries == 0:
    print("You lost. The word was:", word)
