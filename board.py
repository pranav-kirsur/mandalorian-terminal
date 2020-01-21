import numpy as np
from colorama import Fore, Back, Style
from mandalorian import Mandalorian


class Board:
    ''' Creates grid for the game '''

    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.__grid = self.__create_grid(rows, cols)

    def __create_grid(self, rows, cols):
        return np.full((rows, cols), Back.BLUE + " ")
    
    def getrows(self):
        return self.__rows

    def getcols(self):
        return self.__cols

    def refresh_grid(self):
        self.__grid = self.__create_grid(self.__rows, self.__cols)

    def print_grid(self):
        ''' 
            Prints the board
        '''
        for row in self.__grid:
            print("".join(row))

    def render(self):
        ''' Renders the top, grid, and ground and prints it onto the screen'''
        self.__reposition_cursor(0, 0)
        print(Back.YELLOW + (" " * self.__cols))
        self.print_grid()
        print(Back.GREEN + (" " * self.__cols))
        print(Back.RESET, end='')

    def render_object(self, game_object):
        ''' Renders the object onto the grid'''
        x = round(game_object.getx())
        y = round(game_object.gety())
        self.__grid[x: x + game_object.height,
                    y:y + game_object.width] = game_object.shape

    def __reposition_cursor(self, x, y):
        print("\033[%d;%dH" % (x, y), end='')

    def is_touching_ground(self, game_object):
        return round(game_object.getx()) + game_object.height >= self.__rows

    def is_touching_left_edge(self, game_object):
        return round(game_object.gety()) <= 0

    def is_touching_top(self, game_object):
        return round(game_object.getx()) <= 0

    def is_touching_right_edge(self, game_object):
        return round(game_object.gety()) + game_object.width >= self.__cols

    def compute_physics(self, game_object):

        game_object.setvx(game_object.getvx() + game_object.getax() + game_object.gravity - \
            (game_object.drag * game_object.getvx() * game_object.getvx() * (1 if game_object.getvx() > 0 else -1)))
        game_object.setvy(game_object.getvy() + game_object.getay() - \
            (game_object.drag * game_object.getvy() * game_object.getvy() * (1 if game_object.getvy() > 0 else -1)))
        game_object.setx(game_object.getx() + game_object.getvx())
        game_object.sety(game_object.gety() + game_object.getvy())

        if(self.is_touching_ground(game_object)):
            game_object.hit_ground(self.__rows)

        if(self.is_touching_top(game_object)):
            game_object.hit_top()

        if(self.is_touching_left_edge(game_object)):
            game_object.hit_left_edge()

        if(self.is_touching_right_edge(game_object)):
            game_object.hit_right_edge(self.__cols)

    def compute_coin_collisions(self, mandalorian, coins_list):
        for coin in coins_list:
            if coin.is_active:
                if (coin.getx() >= mandalorian.getx()) and (coin.gety() >= mandalorian.gety()) and (coin.getx() < mandalorian.getx() + mandalorian.height) and (coin.gety() < mandalorian.gety() + mandalorian.width):
                    # collision has occurred
                    coin.collect()
                    mandalorian.coins_collected += 1

    def compute_laser_collision(self, mandalorian, laser):
        laser_squares = []
        if(laser.type == 1):
            for i in range(5):
                laser_squares.append((laser.getx(), laser.gety() + i))
        elif(laser.type == 2):
            for i in range(5):
                laser_squares.append((laser.getx() + i, laser.gety()))
        elif(laser.type == 3):
            for i in range(5):
                laser_squares.append((laser.getx() + i, laser.gety() + i))
        elif(laser.type == 4):
            for i in range(5):
                laser_squares.append((laser.getx() + 4 - i, laser.gety() + i))

        has_collision_occured = False

        for sqaure in laser_squares:
            if (sqaure[0] >= mandalorian.getx()) and (sqaure[1] >= mandalorian.gety()) and (sqaure[0] < mandalorian.getx() + mandalorian.height) and (sqaure[1] < mandalorian.gety() + mandalorian.width):
                has_collision_occured = True

        if has_collision_occured:
            if not mandalorian.shield_active:
                mandalorian.lives -= 1
            laser.is_active = False

    def compute_projectile_collision(self, bullet, object):
        bullet_squares = [(bullet.getx(), bullet.gety() + i) for i in range(bullet.width)]

        has_collision_occured = False

        for sqaure in bullet_squares:
            if (sqaure[0] >= object.getx()) and (sqaure[1] >= object.gety()) and (sqaure[0] < object.getx() + object.height) and (sqaure[1] < object.gety() + object.width):
                has_collision_occured = True

        return has_collision_occured

    def compute_speed_boost_collision(self, mandalorian, speed_boost):
        return (speed_boost.getx() >= mandalorian.getx()) and (speed_boost.gety() >= mandalorian.gety()) and (speed_boost.getx() < mandalorian.getx() + mandalorian.height) and (speed_boost.gety() < mandalorian.gety() + mandalorian.width)
