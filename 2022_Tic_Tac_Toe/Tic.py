
#Author: Niket Bachhawat
#Description: A Python program for the classic tic-tac-toe game

#Setting the board up!

def display_board(board):
    print('\n'*100)

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

#Board Setup Completed 

#Taking user input

def player_input():
    holder=''
    while not(holder == 'X' or holder == 'O'):
        holder = input("Hey! \n Choose the holder Player 1 'X' or 'O' \n ").upper()
    # Checking of holder  
    if holder == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

#Putting Position of the input

def place_holder(board, holder, place):
    board[place] = holder

# Checking if Player has won
# All possible condition

def winner_dinner(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark)) 

#Deciding how goes first?
import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

#Places where input available

def space_check(board, position):
    
    return board[position] == ' '


#Full Board

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

#user choice

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

#game heart 

print("Welcome to the game")
start = True
while start:
    # Reset the board
    theBoard = [' '] * 10

    player1_marker, player2_marker = player_input()

    turn = choose_first()

    print(turn + ' will go first.')
    
    play_game = input("Are you ready to play? Y or N. '\n'")
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_holder(theBoard, player1_marker, position)

            if winner_dinner(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations Player 1! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_holder(theBoard, player2_marker, position)

            if winner_dinner(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
    start= False
