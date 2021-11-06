#Write a program (function!) that takes a list and returns a new list that contains all the elements of the
# first list minus all the duplicates.
#Extras:
#Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#Go back and do Exercise 5 (List Overlap) using sets, and write the solution for that in a different function.

#Sets
#In mathematics, a set is a collection of elements where no element is repeated.
#This becomes useful because if you know your data is stored in a set, you are guaranteed to have unique elements.

def setfunc(lists):
    newset = set(lists)
    print(sorted(list(newset)))

def loopfunc(listl):
    newlist = []
    for a in listl:
        if a not in newlist:
            newlist.append(a)
    print(newlist)

setfunc([1, 1, 2, 3, 5, 8, 8, 13, 21, 34, 55, 55, 89, 89])
loopfunc([1, 1, 2, 3, 5, 8, 8, 13, 21, 34, 55, 55, 89, 89])