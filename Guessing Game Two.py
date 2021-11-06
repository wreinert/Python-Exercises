#In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.
#This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100.
#The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
#At the end of this exchange, your program should print out how many guesses it took to get your number.
#As the writer of this program, you will have to choose how your program will strategically guess.
#A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number.
#But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50
#(right in the middle of the range), and then increase / decrease by 1 as needed.
import random as r

my_list = range(1,100)
target = r.randint(1,100)
guess = 0
number_of_loops = 0

while not (len(my_list) == 1 or guess == target):
  center_index = int(len(my_list) / 2)
  guess = my_list[center_index]
  if guess > target:
    my_list = my_list[:center_index]
  elif guess < target:
    my_list = my_list[center_index:]
  number_of_loops += 1

if guess == target:
  print("Found target! Guess = " + str(guess))
else:
  print("Target not found. Last guess = " + str(guess))
print("while loop executed " + str(number_of_loops) + " times")
