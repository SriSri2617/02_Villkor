import random

# 5 Guess a number

def guess_number():
    secret = random.randint(1, 100)
    guesses = 0

    guess = int(input("Enter the number : "))
    while guess != secret:
        guesses += 1

        # version 2 - within 5 close guesses
        if abs(guess - secret) <= 5:
            print("Now it's starting to burn!")


        if guess > secret:
            print("Guess was too high. Try again.")
        else:
            print("Guess was too low. Try again.")

        guess = int(input("Enter the number : "))

    # When correct
    guesses += 1
    print("Correct guess!")
    print("You guessed " + str(guesses) + " times! \n")

guess_number()