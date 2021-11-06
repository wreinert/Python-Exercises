#Take two lists, say for example these two:
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only
# the elements that are common between the lists (without duplicates).
#Make sure your program works on two lists of different sizes.
#Randomly generate two lists to test this

import random

a = random.sample(range(1,30),11)
b = random.sample(range(1,30),13)
new_list = []
print (a)
print (b)

for i in a:
    if i in a and i in b:
        new_list.append(i)

print (new_list)