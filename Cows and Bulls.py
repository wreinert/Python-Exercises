#Create a program that will play the “cows and bulls” game with the user. The game works like this:
#Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”.
# For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
# Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
#Example:
#  Welcome to the Cows and Bulls Game!
#  Enter a number:
#  >>> 1234
#  2 cows, 0 bulls
#  >>> 1256
#  1 cow, 1 bull

import random


number = random.sample(range(9),k=4)
digits = []
string_ints = [str(int) for int in digits] #turning ints in to string for join method

for a in number:
    digits.append(str(a))

print(digits)
print(''.join(digits))

print("Welcome to the Cows and Bulls Game")
#guess = input("Please enter a 4 digit number: ")
#guessList = list(guess)
#print(guessList)

def check():
    guessList = list(input("Please enter a 4 digit number: "))
    counter = 0
    cows = 0
    bulls = 0
    while counter < 4:
        for g in guessList:
            if g == digits[counter]:
                cows += 1
            else:
                bulls += 1
            counter += 1
        print("Cows: " + str(cows) + " Bulls: " + str(bulls))
        if cows >= 4:
            break
        check()

check()




