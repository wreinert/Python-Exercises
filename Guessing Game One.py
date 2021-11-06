#Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
#Extras:
#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

randomnumber = random.randint(1,9)
guess = False
tries = 1

while guess != True:
    userguess = eval(input('Guess a number: '))
    if userguess > randomnumber:
        print('Too high')
        tries += 1
    elif userguess < randomnumber:
        print('Too low')
        tries += 1
    else:
        guess = True

print(f'Correct after {tries} tries')

