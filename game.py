from board import Board
from minmax import MinMax
from alphabeta import AlphaBeta
import time
import random
import numpy as np

# GAME LINK
# http://kevinshannon.com/connect4/



def main(a,b):
    board = Board()
    if b ==1:
        minmax=MinMax(depth=4)
        alphabeta =AlphaBeta(depth=4)
    elif b ==2:
        minmax=MinMax(depth=5)
        alphabeta =AlphaBeta(depth=5)
    elif b ==3:
        minmax=MinMax(depth=6)
        alphabeta =AlphaBeta(depth=6)

    time.sleep(5)
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()
        #print(board.turn)
        #board.turn = 1
        # FOR DEBUG PURPOSES
        board.print_grid(game_board)

        if(a==1):
            col=minmax.get_move(board)
        else:
            col=alphabeta.get_move(board)

        board.select_column(col)




        # YOUR CODE GOES HERE

        # Insert here the action you want to perform based on the output of the algorithm
        # You can use the following function to select a column
        #random_column = random.randint(0, 6)
        #board.select_column(random_column)

        time.sleep(5)


if __name__ == "__main__":
    main()
