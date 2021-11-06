#Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
# and ask if the players want to start a new game)
#rock > scissor
#scissor > paper
#paper > rock

player1w = 0
player2w = 0
games = 0

option1 = "Rock"
option2 = "Paper"
option3 = "Scissor"

while games < 3:
    player1 = input(f"Player 1 pick one: {option1}, {option2}, {option3}")
    player2 = input(f"Player 2 pick one: {option1}, {option2}, {option3}")
    if player1.upper() == option1.upper():
        if player2.upper() == option3.upper():
            print("Player 1 wins")
            player1w += 1
        elif player2.upper() == option2.upper():
            print("Player 2 wins")
            player2w += 1
        elif player2.upper() == option1.upper():
            print("It is a draw")
    elif player1.upper() == option2.upper():
        if player2.upper() == option1.upper():
            print("Player 1 wins")
            player1w += 1
        elif player2.upper() == option3.upper():
            print("Player 2 wins")
            player2w += 1
        elif player2.upper() == option2.upper():
            print("It is a draw")
    elif player1.upper() == option3.upper():
        if player2.upper() == option2.upper():
            print("Player 1 wins")
            player1w += 1
        elif player2.upper() == option1.upper():
            print("Player 2 wins")
            player2w += 1
        elif player2.upper() == option3.upper():
            print("It is a draw")
    else:
        print('Not a valid option')
    games += 1

if player1w > player2w:
    print("Player 1 is best of 3")
else:
    print("Player 2 is best of 3")



