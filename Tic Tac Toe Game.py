#Ask the user to enter coordinates in the form “row,col” - a number, then a comma, then a number.
#Then you can use your Python skills to figure out which row and column they want their piece to be in.
import numpy as np

def check_tictac(game):
    counterex = 0
    counterin = 0
    result = True
    arrayvd = game #had to create this variable, because the vertical and diagonal loops were taking "game" after it had run in horizontal
    #horizontal check:
    for game in game:
        if len(set(game)) == 1:
            if game[counterex] == 1:
                print("player 1 won")
                result = False
            elif game[counterex] == 2:
                print("player 2 won")
                result = False
        counterex += 1
    if result:
        #vertical check:
        verarray = np.array(arrayvd)
        while counterin < 3:
            column = verarray[:,counterin]
            if len(set(column)) == 1:
                if column[counterin] == 1:
                    print("player 1 won")
                    result = False
                elif column[counterin] == 2:
                    print("player 2 won")
                    result = False
            counterin += 1
        if result:
            #diagonal check:
            diag = list(np.diagonal(arrayvd))
            if len(set(diag)) == 1: #check if all elements in diag are equal
                if diag[0] == 1:
                    print("player 1 won")
                    result = False
                elif diag[0] == 2:
                    print("player 2 won")
                    result = False
    return result
#####################Code above should be a class

gameboard = np.zeros((3,3),dtype=int)
winner = False
p1attempts = 0
p2attempts = 1
while winner==False:
    if p1attempts < p2attempts:
        player1 = eval(input("Pick: "))
        if gameboard[player1]==0:
            gameboard[player1] = 1
            p1attempts+=1
        else:
            print('Try again')
    else:
        player2 = eval(input("Pick: "))
        if gameboard[player2]==0:
            gameboard[player2] = 2
            p2attempts+=1
        else:
            print('Try again')
    print(gameboard)
    game_check = check_tictac(gameboard)
    if game_check == False:
        winner = True

