#Implement a function that takes as input three variables, and returns the largest of the three.
#Do this without using the Python max() function!
#The goal of this exercise is to think about some internals that Python normally takes care of for us.
#All you need is some variables and if statements!

a = 1,2,3

checkmax = sorted(list(a))
print(checkmax[len(checkmax)-1])