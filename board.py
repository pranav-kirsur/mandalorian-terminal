import numpy as np
from colorama import Fore, Back, Style
from mandalorian import Mandalorian

class Board:
    ''' Creates grid for the game '''

    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.__grid = self.__create_grid(rows, cols)
        self.__ground_size = 3

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

    def render_scenery(self):
        ''' Renders the background, ceiling, and ground '''
        new_grid = np.full((self.__rows, self.__cols), Back.BLUE + ".")
        new_grid[self.__rows - self.__ground_size:,
                 :] = np.full((self.__ground_size, self.__cols), Back.GREEN + ".")
        new_grid[0,:] = np.full((1,self.__cols), Back.YELLOW + ".")

        self.__grid = new_grid

    def render_mandalorian(self, mandalorian):
        ''' Renders the playing character '''
        
