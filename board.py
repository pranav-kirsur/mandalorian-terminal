import numpy as np
from colorama import Fore, Back, Style
from mandalorian import Mandalorian


class Board:
    ''' Creates grid for the game '''

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.__grid = self.__create_grid(rows, cols)

    def __create_grid(self, rows, cols):
        return np.full((rows, cols), Back.BLUE + " ")

    def refresh_grid(self):
        self.__grid = self.__create_grid(self.rows, self.cols)

    def print_grid(self):
        ''' 
            Prints the board
        '''
        for row in self.__grid:
            print("".join(row))

    def render(self):
        ''' Renders the top, grid, and ground and prints it onto the screen'''
        self.reposition_cursor(0, 0)
        print(Back.YELLOW + (" " * self.cols))
        self.print_grid()
        print(Back.GREEN + (" " * self.cols))
        print(Back.RESET, end='')

    def render_object(self, game_object):
        ''' Renders the object onto the grid'''
        x = round(game_object.x)
        y = round(game_object.y)
        self.__grid[x: x + game_object.height,
                    y:y + game_object.width] = game_object.shape

    def reposition_cursor(self, x, y):
        print("\033[%d;%dH" % (x, y), end='')

    def is_touching_ground(self, game_object):
        return round(game_object.x) + game_object.height >= self.rows

    def is_touching_left_edge(self, game_object):
        return round(game_object.y) <= 0

    def is_touching_top(self, game_object):
        return round(game_object.x) <= 0

    def is_touching_right_edge(self, game_object):
        return round(game_object.y) + game_object.width >= self.cols

    def compute_physics(self, game_object):

        game_object.vx += game_object.ax + game_object.gravity - \
            (game_object.drag * game_object.vx * game_object.vx)
        game_object.vy += game_object.ay - \
            (game_object.drag * game_object.vy * game_object.vy)
        game_object.x += game_object.vx
        game_object.y += game_object.vy

        if(self.is_touching_ground(game_object)):
            game_object.hit_ground(self.rows)

        if(self.is_touching_top(game_object)):
            game_object.hit_top()

        if(self.is_touching_left_edge(game_object)):
            game_object.hit_left_edge()

        if(self.is_touching_right_edge(game_object)):
            game_object.hit_right_edge(self.cols)

    def compute_coin_collisions(self, mandalorian, coins_list):
        for coin in coins_list:
            if coin.is_active:
                if (coin.x >= mandalorian.x) and (coin.y >= mandalorian.y) and (coin.x < mandalorian.x + mandalorian.height) and (coin.y < mandalorian.y + mandalorian.width):
                    # collision has occurred
                    coin.collect()
                    mandalorian.coins_collected += 1

    def compute_laser_collision(self, mandalorian, laser):
        laser_squares = []
        if(laser.type == 1):
            for i in range(5):
                laser_squares.append((laser.x, laser.y + i))
        elif(laser.type == 2):
            for i in range(5):
                laser_squares.append((laser.x + i, laser.y))
        elif(laser.type == 3):
            for i in range(5):
                laser_squares.append((laser.x + i, laser.y + i))
        elif(laser.type == 4):
            for i in range(5):
                laser_squares.append((laser.x + 4 - i, laser.y + i))

        has_collision_occured = False

        for sqaure in laser_squares:
            if (sqaure[0] >= mandalorian.x) and (sqaure[1] >= mandalorian.y) and (sqaure[0] < mandalorian.x + mandalorian.height) and (sqaure[1] < mandalorian.y + mandalorian.width):
                has_collision_occured = True

        if has_collision_occured:
            if not mandalorian.shield_active:
                mandalorian.lives -= 1
            laser.is_active = False

    def compute_bullet_collision(self, bullet, object):
        bullet_squares = [(bullet.x, bullet.y), (bullet.x, bullet.y + 1)]

        has_collision_occured = False

        for sqaure in bullet_squares:
            if (sqaure[0] >= object.x) and (sqaure[1] >= object.y) and (sqaure[0] < object.x + object.height) and (sqaure[1] < object.y + object.width):
                has_collision_occured = True

        return has_collision_occured