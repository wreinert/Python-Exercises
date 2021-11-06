#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.
import random

#a = range(random.randrange(0,5),random.randrange(6,20),random.randrange(1,3))
#for x in a:
#    print(x)
#new_list = [a[0],a[len(a)-1]]
#print(new_list)

def digits(start,stop,pace):
    a = range(start, stop, pace)
    new_list = [a[0],a[len(a)-1]]
    print(new_list)

digits(random.randrange(0, 5), random.randrange(6, 20), random.randrange(1, 3))