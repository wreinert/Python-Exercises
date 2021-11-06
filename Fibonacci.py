#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
#Take this opportunity to think about how you can use functions.
#Make sure to ask the user to enter the number of numbers in the sequence to generate.
#(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous
#two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
try:

    def fibonaccif(length):
        fibonacci = []
        sequence = 0
        if length == 1:
            fibonacci.append(1)
            print(fibonacci)
        elif length == 2:
            fibonacci.extend([1,1])
            print(fibonacci)
        elif length >2:
            fibonacci=[1,1]
            while len(fibonacci) < length:
                fibonacci.append(fibonacci[sequence]+fibonacci[sequence+1])
                sequence += 1
            print(fibonacci)
        else:
            print('Nothing')

    fibonaccif(int(input('Pick a number: ')))

except ValueError:
    print("You did not enter a number")