from person import GameObject
import numpy as np
from colorama import Fore, Back, Style


class Mandalorian(GameObject):

    def __init__(self, x, y, vx, vy):
        GameObject.__init__(self, x, y, vx, vy)
        self.shape = np.array(
            [
                [Back.WHITE + '/', Back.WHITE + 'O', Back.WHITE + '\\'],
                [Back.WHITE + '-', Back.WHITE + '-', Back.WHITE + '-'],
                [Back.WHITE + '-', Back.WHITE + '-', Back.WHITE + '-']
            ])
        self.height = 3
        self.width = 3
        self.gravity = 0.3
        self.drag = 0.05
