import numpy as np

class TicTacCheck:
    def __init__(self):



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