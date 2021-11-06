#Write a program (using functions!) that asks the user for a long string containing multiple words.
#Print back to the user the same string, except with the words in backwards order.
#For example, say I type the string:
#My name is Michele
#Then I would see the string:
#Michele is name My

def reverseString(sentence):
    wordlist = sentence.split(" ")
    reverse = list(reversed(wordlist))
    print("Your sentence: "+str(wordlist)+'\n'+"Reversed: "+str(reverse))
    newstring = " ".join(reverse)
    print(newstring)
    
reverseString(input("Enter a string: "))