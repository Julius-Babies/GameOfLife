import time

from patterns import *
from tools import *

WIDTH = 50
HEIGHT = 20

if __name__ == "__main__":
    board = generate_pulsator(WIDTH, HEIGHT)
    while True:
        # new round
        old_board = clone_array(board)
        print(get_board_visual(board))
        for x in range(len(board)):
            for y in range(len(board[0])):
                neighbours = get_neighbours(old_board, x, y)
                if old_board[x][y] == 0:
                    if neighbours == 3:
                        board[x][y] = 1  # come to live
                else:
                    if neighbours < 2:
                        board[x][y] = 0  # underpopulation
                    elif neighbours > 3:
                        board[x][y] = 0  # overpopulation
                    else:
                        board[x][y] = 1  # stay

        time.sleep(0.4)
