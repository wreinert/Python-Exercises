number = eval(input('Insert number: '))
check = eval(input('Insert a divider: '))

if number%4 == 0:
    print('Multiplo de quatro')
elif number%2 == 0:
    print('O numero é par')
else:
    print('O numero é impar')

if number%check == 0:
    print(str(number)+' evenly divided by '+str(check))
else:
    print(str(number)+' not evenly divided by '+str(check))