from person import Person
import numpy as np
from colorama import Fore, Back, Style


class Mandalorian(Person):

    def __init__(self, x, y):
        Person.__init__(self, x, y)
        self.shape = np.array(
            [
                [Back.WHITE + '/', Back.WHITE + 'O', Back.WHITE + '\\'],
                [Back.WHITE + '-', Back.WHITE + '-', Back.WHITE + '-'],
                [Back.WHITE + '-', Back.WHITE + '-', Back.WHITE + '-']
            ])
        self.height = 3
        self.width = 3
        self.vx = 0
        self.vy = 0
        self.ax = 0.3
        self.ay = 0
