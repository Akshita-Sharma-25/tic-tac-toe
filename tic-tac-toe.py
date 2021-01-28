''' 
A two player based tic-tac-toe game which chooses the player at random 
the position of the dashboard starts from bottom left = 1 and upper right = 9
also checks whether the place entered by the player is empty or not.
'''
from random import randint
# displaying tic-tac-toe board
def drawboard(board):
    print('\n'*100)
    print('-----------')
    print('   |   |')
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])
    print('   |   |')
    print('-----------')

# choosing the mark to display
def mark():
    ''' Takes input from the user as "X" or "O" and return the tuple of mark assigned to the two user'''
    marker = ''
    while not(marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# placing the marker        
def place_marker(board, marker, position):
    ''' Takes marker and position from the user and place the marker at the given position'''
    board[position] = marker

# choosing randomly which player will go first     
def first_player():
    if randint(0,1) == 0:
        return 'player1'
    return 'player2'

# checking whether the player won or not
def win_check(board, mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

# checking if the position is free to enter the mark or not    
def free_space(board, position):
    if board[position] == ' ':
        return True
    else:
        print('the place is full')
        return False

# checking whether the board is fully occupied or not    
def board_full(board):
    for i in range(1, 10):
        if free_space(board, i):
            return False
    return True

# asking players choice where he/ she wants to enter the mark    
def player_choice(board, player):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not free_space(board, position):
        position = int(input(f'Choose your next position {player}: (1-9) '))
    return position

# asking for replay
def replay():
    result = input('Do you want to play again? Enter Y or N: ').upper
    if result == 'Y':
        return True
    else:
        return False

# And the game begins!!
print('WELCOME TO TIC-TAC-TOE!')
while True:
    board = [' ']*10 #assigning all the position with space
    player1_mark,player2_mark = mark()
    turn = first_player()
    print(turn + ' will go first.')

    play_game=input('Do you want to play? "Y" or"N"').upper()
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'player1':
            drawboard(board)
            position = player_choice(board, turn)
            place_marker(board,player1_mark,position)
            if win_check(board,player1_mark):
                drawboard(board)
                print('Congratulations! player1 have won the game!')
                game_on = False
            else:
                if board_full(board):
                    drawboard(board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'player2'
        else:
            drawboard(board)
            position = player_choice(board, turn)
            place_marker(board,player2_mark,position)
            if win_check(board,player2_mark):
                drawboard(board)
                print('Congratulations! player2 have won the game!')
                game_on = False
            else:
                if board_full(board):
                    drawboard(board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'player1'
    if not replay():
        break            

