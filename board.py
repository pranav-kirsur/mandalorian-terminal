import numpy as np
from colorama import Fore, Back, Style
from mandalorian import Mandalorian


class Board:
    ''' Creates grid for the game '''

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.__grid = self.__create_grid(rows, cols)
        self.ground_size = 3

    def __create_grid(self, rows, cols):
        return np.full((rows, cols), Back.BLUE + ".")

    def print_grid(self, window_left, window_right):
        ''' Prints part of the board in the window given by the given parameters
            The interval is [window_left, window_right)
        '''
        section_to_print = self.__grid[:, window_left: window_right]

        for row in section_to_print:
            for elem in row:
                print(elem, end='')
            print('\n', end='')

        print(Back.RESET, end='')

    def render_scenery(self):
        ''' Renders the background, ceiling, and ground '''
        new_grid = np.full((self.rows, self.cols), Back.BLUE + ".")
        new_grid[self.rows - self.ground_size:,
                 :] = np.full((self.ground_size, self.cols), Back.GREEN + ".")
        new_grid[0, :] = np.full((1, self.cols), Back.YELLOW + ".")

        self.__grid = new_grid

    def render_mandalorian(self, mandalorian: Mandalorian):
        ''' Renders the playing character '''
        x = round(mandalorian.x)
        y = round(mandalorian.y)
        self.__grid[x: x + mandalorian.height,
                    y:y + mandalorian.width] = mandalorian.shape

    def reposition_cursor(self, x, y):
        print("\033[%d;%dH" % (x, y), end='')

    def do_physics(self, mandalorian: Mandalorian):

        mandalorian.x += mandalorian.vx
        mandalorian.y += mandalorian.vy
        mandalorian.vx += mandalorian.ax
        mandalorian.vy += mandalorian.ay

        # if on ground
        if(mandalorian.x + mandalorian.height + self.ground_size >= self.rows):
            mandalorian.x = self.rows - self.ground_size - mandalorian.height
            mandalorian.vx = 0
            mandalorian.ax = 0
