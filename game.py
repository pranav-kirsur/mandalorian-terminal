from board import Board
from mandalorian import Mandalorian
import os
from time import sleep
from colorama import init
from input import Get

init()


ttyrows, ttycolumns = os.popen('stty size', 'r').read().split()
ttyrows, ttycolumns = int(ttyrows), int(ttycolumns)

game_board = Board(rows=40, cols=1000)
os.system('clear')
player = Mandalorian(x=3, y=3)
game_board.render_scenery()
game_board.render_mandalorian(player)
game_board.print_grid(0, ttycolumns)

while True:
    sleep(0.1)
    
    game_board.render_scenery()

    input_char = Get()
    if(input_char == 'w'):
        player.x -= 1

    game_board.do_physics(player)
    game_board.render_mandalorian(player)
    game_board.reposition_cursor(0, 0)
    game_board.print_grid(0, ttycolumns)


