#As you may have guessed, we are trying to build up to a full tic-tac-toe board.
#However, this is significantly more than half an hour of coding, so we’re doing it in pieces.
#Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe,
#not worrying about how the moves were made.
#If a game of Tic Tac Toe is represented as a list of lists, like so:
#game = [[1, 2, 0],
#	     [2, 1, 0],
#	     [2, 1, 1]]
#where a 0 means an empty square, a 1 means that player 1 put their token in that space,
# and a 2 means that player 2 put their token in that space.
#Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board,
#tell me whether anyone has won, and tell me which player won, if any.
#A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal.
#Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.
import numpy

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
            elif game[counterex] == 2:
                print("player 2 won")
        counterex += 1
    if result:
        #vertical check:
        verarray = numpy.array(arrayvd)
        while counterin < 3:
            column = verarray[:,counterin]
            if len(set(column)) == 1:
                if column[counterin] == 1:
                    print("player 1 won")
                elif column[counterin] == 2:
                    print("player 2 won")
            counterin += 1
        if result:
            #diagonal check:
            diag = list(numpy.diagonal(arrayvd))
            if len(set(diag)) == 1: #check if all elements in diag are equal
                if diag[0] == 1:
                    print("player 1 won")
                elif diag[0] == 2:
                    print("player 2 won")

#teste
#check_tictac([[1,2,0],[2,1,0],[2,1,1]])
