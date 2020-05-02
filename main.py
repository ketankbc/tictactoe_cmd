import os

board = ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def show_board(board):
   print(f"{board[1]} |  {board[2]}  | {board[3]}")
   print(f"{board[4]} |  {board[5]}  | {board[6]}")
   print(f"{board[7]} |  {board[8]}  | {board[9]}")

def clear_bord():
    os.system('clear') 

def take_input():
    value=''
    while value!='X' and value!='O':
        value=input('Please enter your mark either "X" or "O"\n')

    if value=='X':
        print('Player 1 is X and he/she will play first')
    else:
        print('Player 1 is O and he/she will play first')

def update_board(value,place):
    global board
    if value=='X':
        board[place]='X'
    else:
        board[place]='O'

def check_place_value(place):
    '''
    This function checks whether the input board place is vacant or not.
    also checks whether input value is between 1 to 9 only.
    if these conditions meet then only return true or else return false.
    '''
    if type(place) is not int:
        print('*****Please enter value from 1 to 9 only')
        return False 
    elif board[place]!=' ':
        print('Please choose different place as this place is already occupied')
        return False
    else:
        return True

def start_game():
    counter=0
    show_board(board)
    for round in board:
        if counter%2==0:
            flag=False

            while not flag:
                place=input('Player 1 turn:\n')
                flag=check_place_value(place)
            update_board('X',place)

        else:
            flag=False

            while not flag:
                place=input('Player 2 turn:\n')
                flag=check_place_value(place)
            update_board('O',place)
        counter+=1
        show_board(board)
    

clear_bord()
take_input()
start_game()

#show_board(board)
#clear_bord()