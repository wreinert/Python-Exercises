#Let’s say the word the player has to guess is “EVAPORATE”.
# For this exercise, write the logic that asks a player to guess a letter and displays letters in the clue word
# that were guessed correctly. For now, let the player guess an infinite number of times until they get the entire word.
# As a bonus, keep track of the letters the player guessed and display a different message if the player tries to guess
# that letter again. Remember to stop the game when all the letters have been guessed correctly!

import random

with open("sowpods.txt",'r') as sp:
    line = sp.readlines()
    word = line[random.randint(0,len(line))]
    #print(word)

hiddenword = list(word.strip())
#print(hiddenword)
result = False
show = ['-']*len(hiddenword)
guesses = []
while result == False:
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
        print(show)
        if hiddenword == show:
            result = True
            print(f"The word is: {''.join(show)}")



