#This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4.
#Time for some fake graphics! Let’s say we want to draw game boards that look like this:
'''
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
 '''
#This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).
#Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

counter = 0
graphics = [" ","---","|"]
#linhas
def linhas(userchoice):
    print(graphics[0]+((graphics[0]+graphics[1])*userchoice),"\n",(graphics[2]+graphics[0]*3)*(userchoice+1))

#colunas
choice = eval(input("Enter number: "))
while counter < choice:
    linhas(choice)
    counter +=1
    if counter >= choice:
        print(graphics[0] + ((graphics[0] + graphics[1]) * choice))