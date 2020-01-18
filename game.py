from board import Board
from mandalorian import Mandalorian
import os
from time import sleep
from colorama import init
from kbhit import KBHit
from coin import Coin
from laser import Laser
from bullet import Bullet

init()


ttyrows, ttycolumns = os.popen('stty size', 'r').read().split()
ttyrows, ttycolumns = int(ttyrows), int(ttycolumns)

os.system('clear')
game_board = Board(rows=ttyrows - 3, cols=ttycolumns)
game_board.render()

player = Mandalorian(3, 3, 0, 0)
kb = KBHit()


coins_list = [Coin(15, ttycolumns - 1, 0, -1), Coin(23, ttycolumns - 1, 0, -1)]
lasers_list = [Laser(40, ttycolumns - 7, 0, -1, 1), Laser(50, ttycolumns - 7, 0, -1, 2),
               Laser(30, ttycolumns - 7, 0, -1, 3), Laser(20, ttycolumns - 7, 0, -1, 4)]
bullets_list = []

while True:
    sleep(0.1)
    if kb.kbhit():
        char = kb.getch()
        if(char == 'w'):
            player.vx -= 2
        elif(char == 'a'):
            player.vy -= 1
        elif(char == 'd'):
            player.vy += 1
        elif(char == 'b'):
            bullets_list.append(Bullet(player.x , player.y + 3, 0, 3))

    game_board.refresh_grid()

    game_board.compute_physics(player)

    for coin in coins_list:
        if(coin.is_active):
            game_board.compute_physics(coin)

    for laser in lasers_list:
        if(laser.is_active):
            game_board.compute_physics(laser)

    for bullet in bullets_list:
        if(bullet.is_active):
            game_board.compute_physics(bullet)

    game_board.compute_coin_collisions(player, coins_list)

    for laser in lasers_list:
        if(laser.is_active):
            game_board.compute_laser_collision(player, laser)

    for laser in lasers_list:
        if(laser.is_active):
            game_board.render_object(laser)

    for coin in coins_list:
        if(coin.is_active):
            game_board.render_object(coin)

    for bullet in bullets_list:
        if(bullet.is_active):
            game_board.render_object(bullet)

    game_board.render_object(player)

    game_board.render()
    print(player.lives, end="")
