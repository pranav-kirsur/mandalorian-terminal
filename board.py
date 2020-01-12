import numpy as np
from colorama import Fore, Back, Style


class Board:
    ''' Creates grid for the game '''

    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.__grid = self.__create_grid(rows, cols)

    def __create_grid(self, rows, cols):
        return np.full((rows, cols), ".")

    def print_board(self, window_left, window_right):
        ''' Prints part of the board in the window given by the given parameters
            The interval is [window_left, window_right)
        '''
        section_to_print = self.__grid[:, window_left: window_right]

        for row in section_to_print:
            for elem in row:
                print(Back.BLUE + elem, end='')
            print('\n', end='')
