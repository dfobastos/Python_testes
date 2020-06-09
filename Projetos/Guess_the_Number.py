import random


"""

Guess the Number:

"""

number = random.randrange(1,50)
guess = int(input("Guess a number between 1 and 50: "))

while number != guess:
    if number > guess:
        print('You need to Guess higher.')
        guess = int(input("Guess a number between 1 and 50: "))

    else:
        print('You need to Guess lower.')
        guess = int(input("Guess a number between 1 and 50: "))

print('You Guessed the number correctly!')






