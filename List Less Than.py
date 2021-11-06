#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#number = 0
#for number in a:
#    if number < 5:
#        print(str(number))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

position = 0
number = 0
user_pick = eval(input('Enter a number: '))

for number in a:
    if number < user_pick:
        position += 1
        b.append(number)
print(str(b))