from board import Board
from mandalorian import Mandalorian
import os
from time import sleep
from colorama import init
from kbhit import KBHit
from coin import Coin
from laser import Laser
from bullet import Bullet
from speedboost import Speedboost
from magnet import Magnet
from boss import Boss

import random
import time

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
speed_boost_list = [Speedboost(20, ttycolumns - 6, 0, -1)]
magnets_list = []
boss_list = []

num_frames = 0
is_shield_available = True
last_shield_activation_time = 0

speed_multiplier = 1

has_boss_arrived = False


while True:
    num_frames += 1
    sleep(0.0175)

    if(time.time() - last_shield_activation_time > 10):
        player.shield_active = False

    if(time.time() - last_shield_activation_time >= 70):
        is_shield_available = True

    # Spawn objects

    if(num_frames == 500):
        # boss arrives
        has_boss_arrived = True
        temp_boss = Boss(0, 0, 0, 0)
        boss_list = [Boss(game_board.rows - temp_boss.height,
                          game_board.cols - temp_boss.width, 0, 0)]

    if(num_frames % 50 == 0 and not has_boss_arrived):
        # spawn some coins
        rownum = random.randint(0, game_board.rows - 4)
        for i in range(3):
            coins_list.append(
                Coin(rownum + i, game_board.cols - 1, 0, -1 * speed_multiplier))

    if(num_frames % 50 == 25 and not has_boss_arrived):
        # spawn lasers
        rownum = random.randint(0, game_board.rows - 6)
        laser_type = random.randint(1, 4)
        lasers_list.append(
            Laser(rownum, game_board.cols - 6, 0, -1 * speed_multiplier, laser_type))

    if(num_frames == 100 and not has_boss_arrived):
        # spawn random magnet
        magnets_list = [Magnet(random.randint(
            0, game_board.rows - 4), ttycolumns - 1, 0, -1)]

    if kb.kbhit():
        char = kb.getch()
        if(char == 'w'):
            player.vx -= 2
        elif(char == 'a'):
            player.vy -= 1
        elif(char == 'd'):
            player.vy += 1
        elif(char == 'b'):
            bullets_list.append(Bullet(player.x, player.y + 3, 0, 2))
        elif(ord(char) == 32):
            if(not player.shield_active and is_shield_available):
                player.shield_active = True
                last_shield_activation_time = time.time()
                is_shield_available = False

    game_board.refresh_grid()

    # magnet attracts player
    for magnet in magnets_list:
        if magnet.is_active:
            magnet.attract(player)

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

    for speed_boost in speed_boost_list:
        if speed_boost.is_active:
            game_board.compute_physics(speed_boost)

    for magnet in magnets_list:
        if magnet.is_active:
            game_board.compute_physics(magnet)

    for boss in boss_list:
        boss.adjustposition(player.x, game_board.rows)

    game_board.compute_coin_collisions(player, coins_list)

    for speed_boost in speed_boost_list:
        if speed_boost.is_active:
            if (game_board.compute_speed_boost_collision(player, speed_boost)):
                speed_multiplier = 2
                speed_boost.is_active = False

    for bullet in bullets_list:
        if bullet.is_active:
            for laser in lasers_list:
                if laser.is_active:
                    if(game_board.compute_bullet_collision(bullet, laser)):
                        laser.is_active = False
                        bullet.is_active = False

    for laser in lasers_list:
        if(laser.is_active):
            game_board.compute_laser_collision(player, laser)

    for laser in lasers_list:
        if(laser.is_active):
            game_board.render_object(laser)

    for coin in coins_list:
        if(coin.is_active):
            game_board.render_object(coin)

    for speed_boost in speed_boost_list:
        if speed_boost.is_active:
            game_board.render_object(speed_boost)

    for magnet in magnets_list:
        if magnet.is_active:
            game_board.render_object(magnet)

    for boss in boss_list:
        game_board.render_object(boss)

    for bullet in bullets_list:
        if(bullet.is_active):
            game_board.render_object(bullet)

    game_board.render_object(player)

    game_board.render()


    # clear dead objects
    new_lasers_list = []
    new_coins_list = []
    new_bullets_list = []

    for laser in lasers_list:
        if(laser.is_active):
            new_lasers_list.append(laser)

    for coin in coins_list:
        if(coin.is_active):
            new_coins_list.append(coin)

    for bullet in bullets_list:
        if(bullet.is_active):
            new_bullets_list.append(bullet)

    coins_list = new_coins_list
    bullets_list = new_bullets_list
    lasers_list = new_lasers_list

    print(player.lives, player.shield_active, end="")
