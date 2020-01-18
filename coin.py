from person import GameObject
from colorama import Fore, Back, Style
import numpy as np


class Coin(GameObject):
    def __init__(self, x, y, vx, vy):
        GameObject.__init__(self, x, y, vx, vy)
        self.is_active = True
        self.height = 1
        self.width = 1
        self.shape = np.array([[Back.YELLOW + '$']])
        self.gravity = 0
        self.drag = 0

    def hit_left_edge(self):
        self.is_active = 0

    def collect(self):
        self.is_active = False

    def hit_top(self):
        return

    def hit_ground(self, rows):
        return
