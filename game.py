from board import Board
import os
from colorama import init
init()


ttyrows, ttycolumns = os.popen('stty size', 'r').read().split()
ttyrows, ttycolumns = int(ttyrows), int(ttycolumns)

game_board = Board(rows=40, cols=1000)
os.system('clear')
game_board.print_board(0, ttycolumns)
