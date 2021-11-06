#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
#(If you don’t know what a divisor is, it is a number that divides evenly into another number.
#For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

number = eval(input('Please pick a number: '))
divisor_list = []
divisor = 1

for divisor in range(1, number+1):
    if number%divisor == 0:
        divisor_list.append(divisor)
        divisor += 1
print(str(divisor_list))


