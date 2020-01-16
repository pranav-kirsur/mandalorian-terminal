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
