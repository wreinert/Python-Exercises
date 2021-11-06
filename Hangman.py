#In this exercise, we will finish building Hangman.
# In the game of Hangman, the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.
#Only let the user guess 6 times, and tell the user how many guesses they have left.
#Keep track of the letters the user guessed. If the user guesses a letter they already guessed,
# don’t penalize them - let them guess again.
#Optional additions:
#When the player wins or loses, let them start a new game.
#Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman.
# This is challenging - do the other parts of the exercise first!
#Your solution will be a lot cleaner if you make use of functions to help you!

import random


def checkTries(tries):
    if tries == 0:
        print("------\n|\n|\n|")
    elif tries == 1:
        print("------\n|    O\n|\n|")
    elif tries == 2:
        print("------\n|    O\n|    |\n|")
    elif tries == 3:
        print("------\n|    O\n|   /|\n|")
    elif tries == 4:
        print("------\n|    O\n|   /|\ \n|")
    elif tries == 5:
        print("------\n|    O\n|   /|\ \n|   /")
    elif tries == 6:
        print("------\n|    X\n|   /|\ \n|   / \ ")

with open("sowpods.txt",'r') as sp:
    line = sp.readlines()
    word = line[random.randint(0,len(line))]
    #print(word)

hiddenword = list(word.strip())
#print(hiddenword)
result = False
show = ['-']*len(hiddenword)
guesses = []
tries = 0
while result == False and tries < 6:
    counter = 0
    guess = input('Pick a letter: ').upper()
    if guess in guesses:
        print('Try another letter')
    else:
        if guess in hiddenword:
            while counter < len(hiddenword):
                if guess == hiddenword[counter]:
                    show[counter] = guess
                counter += 1
            guesses.append(guess)
        else:
           tries += 1
           guesses.append(guess)
           checkTries(tries)
        print(show)
        if hiddenword == show:
            result = True
            print(f"The word is: {''.join(show)}")
        if tries == 6:
            print('Game over: out of tries')
            print(f"The word is: {''.join(hiddenword)}")

