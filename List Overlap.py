#Write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
#Make sure your program works on two lists of different sizes.

#Extras:
#Randomly generate two lists to test this
#Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_list = []
counter = 0
number = a[counter]

for number in a:
    if number in b:
        if number not in common_list:
            common_list.append(number)
            counter += 1

print(str(common_list))


