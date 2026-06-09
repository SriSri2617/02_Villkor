import random

# 1. add the numbers and if sum pass 21 it should stop total <= 21
def game21():
    # Start with total = 0 and an empty list to store the numbers
    total = 0
    numbers = []

    number = 1
    # Keep adding numbers until the total reaches 21
    while total < 21:
        try:
            # add the current number to the total
            total += number

            # store the number in the list
            numbers.append(number)
            number += 1


        except ValueError:
            print("Please enter a number")

    return numbers, total


# Version 2: instead of using the number series, randomize numbers between 1 and 13.

def game21_random():
    total = 0
    numbers = []

    while total < 21:
        card = random.randint(1, 13)
        numbers.append(card)
        total += card
        numbers.append(card)

    return numbers, total

