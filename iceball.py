from person import GameObject
import numpy as np
from colorama import Fore, Back, Style


class Iceball(GameObject):
    def __init__(self, x, y, vx, vy):
        GameObject.__init__(self, x, y, vx, vy)

        self._shape = np.full((1, 4), Back.CYAN + " ")
        self.__height = 1
        self.__width = 4
        self._active = True
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
    
    def hit_right_edge(self, cols):
        self._active = False

    def hit_top(self):
        return
    
    def hit_ground(self, rows):
        return
