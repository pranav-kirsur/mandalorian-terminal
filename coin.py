from person import GameObject
from colorama import Fore, Back, Style
import numpy as np


class Coin(GameObject):
    def __init__(self, x, y, vx, vy):
        GameObject.__init__(self, x, y, vx, vy)
        self._active = True
        self.__height = 1
        self.__width = 1
        self._shape = np.array([[Back.YELLOW + '$']])
        self._gravity = 0
        self._drag = 0

    def is_active(self):
        return self._active

    def getheight(self):
        return self.__height
    
    def getwidth(self):
        return self.__width

    def hit_left_edge(self):
        self._active = False

    def collect(self):
        self._active = False

    def hit_top(self):
        return

    def hit_ground(self, rows):
        return
