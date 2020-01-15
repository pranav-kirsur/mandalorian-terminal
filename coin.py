from person import GameObject
from colorama import Fore, Back, Style
import numpy as np


class Coin(GameObject):
    def __init__(self, x, y, vx, vy):
        GameObject.__init__(self, x, y, vx, vy)
        self.is_collected = False
        self.height = 1
        self.width  = 1
        self.shape = np.array([[Back.YELLOW + '$']])
        self.gravity = 0
        self.drag = 0