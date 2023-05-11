import numpy as np


ROW_COUNT=6
COLUMN_COUNT=7

def create_board():
    board=np.zeros((6,7))
    return board


def drop_piece():
    pass


def is_valid_location(board,col):
    return board[5][col]==0


def get_next_open_row():
    for r in range(ROW_COUNT):
        if board[r][col]==0
            return r

board=create_board()
print(board)
game_over=False
turn=0


while not game_over:
    #Ask for P1 input
    if turn==0:
        col= int(input("Player 1 make your selection (0-6):"))

    #Ask for P2 input
    else:
         col= int(input("Player 2 make your selection (0-6):"))

    turn+=1
    turn=turn%2
