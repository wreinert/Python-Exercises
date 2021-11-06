#Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
#can only be divided by 1 and itself.
# You can (and should!) use your answer to Exercise 4 (Divisors) to help you.
# Take this opportunity to practice using functions, described below.

#Sys is used to end the iteration on line 17, otherwise the function, if the rest is 0, would return "is not prime" and then
#return to the initial if until all iterations are finished and return "is prime" as well.
import sys

def primecheck(number):
    if number > 0:
        for x in range(2, number - 1):  # this range excludes number and 1, both of which number is divisible by
            if number % x != 0:  # If number isn't evenly divisible by x, start over with the next one
                continue
            elif number % x == 0:  # If number is evenly divisible by x, it can't be prime
                sys.exit("The number is not prime.")
        sys.exit("The number is prime.")  # number wasn't evenly divisible by any x, so it's prime
    elif number == 0:
        sys.exit("The number is not prime.")  # According to the Google, 0 is not prime
    else:  # if number is less than 0, the number is not prime (according to the Google).
        sys.exit("The number is not prime.")

primecheck(int(input("Please enter a number" + "\n" + ">>>")))
