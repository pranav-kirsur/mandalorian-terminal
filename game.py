from board import Board
from mandalorian import Mandalorian
import os
from time import sleep
from colorama import init
from kbhit import KBHit

init()


ttyrows, ttycolumns = os.popen('stty size', 'r').read().split()
ttyrows, ttycolumns = int(ttyrows), int(ttycolumns)

os.system('clear')
game_board = Board(rows=ttyrows - 3, cols=ttycolumns)
game_board.render()

player = Mandalorian(3,3,0,0)
kb = KBHit()

while True:
    if kb.kbhit():
        char = kb.getch()
        if(char == 'w'):
            player.vx -= 2
        elif(char == 'a'):
            player.vy -= 2 
        elif(char == 'd'):
            player.vy+= 2
    game_board.compute_physics(player)
    game_board.render_object(player)
    game_board.render()
    print(player.vx, player.vy)




