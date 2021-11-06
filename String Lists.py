#Ask the user for a string and print out whether this string is a palindrome or not.

string = input('Enter a string: ')

#if string[0] == string[len(string)-1]:
#    print('Is palindrome')
#else:
#    print('Is not palindrome')

if string[0] == string[-1]:
    print('Is palindrome')
else:
    print('Is not palindrome')