from board import Board
from mandalorian import Mandalorian
import os
from colorama import init
init()


ttyrows, ttycolumns = os.popen('stty size', 'r').read().split()
ttyrows, ttycolumns = int(ttyrows), int(ttycolumns)

game_board = Board(rows=40, cols=1000)
os.system('clear')
player = Mandalorian(x=3, y=3)
game_board.render_scenery()
game_board.render_mandalorian(player)
game_board.print_grid(0, ttycolumns)
