#Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number.
#The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
#Extras: Use binary search.

import random as r

orderedlist = list(range(r.randint(1,5),20,r.randint(2,3)))
number = r.randint(1,20)
print("Number: "+str(number)+' / List: '+str(orderedlist))

def numbercheck():
    if number in orderedlist:
        if orderedlist[(int(len(orderedlist) / 2))] == number:
            print("It's a match")
        elif orderedlist[int(len(orderedlist) / 2)] > number:
            if number in orderedlist[0:int(len(orderedlist) / 2)]:
                print("It's a match 2")
        elif orderedlist[int(len(orderedlist) / 2)] < number:
            if number in orderedlist[int(len(orderedlist) / 2):len(orderedlist)]:
                print("It's a match 3")
    else:
        print("There's no match")

numbercheck()


