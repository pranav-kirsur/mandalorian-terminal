from person import GameObject
import numpy as np
from colorama import Fore, Back, Style


class Mandalorian(GameObject):

    def __init__(self, x, y, vx, vy):
        GameObject.__init__(self, x, y, vx, vy)
        self.shape1 = np.array(
            [
                [Back.WHITE + '/', Back.WHITE + 'O', Back.WHITE + '\\'],
                [Back.WHITE + '-', Back.WHITE + '-', Back.WHITE + '-'],
                [Back.WHITE + '-', Back.WHITE + '-', Back.WHITE + '-']
            ])
        self.shape2 = np.array(
            [
                [Back.BLACK + '/', Back.BLACK + 'O', Back.BLACK + '\\'],
                [Back.BLACK + '-', Back.BLACK + '-', Back.BLACK + '-'],
                [Back.BLACK + '-', Back.BLACK + '-', Back.BLACK + '-']
            ])
        self.shape = self.shape1
        self.__height = 3
        self.__width = 3
        self._gravity = 0.115
        self._drag = 0.05
        self.coins_collected = 0
        self.lives = 3
        self.shield_active = False

    def getheight(self):
        return self.__height
    
    def getwidth(self):
        return self.__width

    def hit_ground(self, rows):
        self._x = rows - self.__height
        self._vx = min(0, self._vx)
        self._ax = min(0, self._ax)

    def hit_left_edge(self):
        self._y = 0
        self._vy = max(0, self._vy)
        self._ay = max(0, self._ay)

    def hit_top(self):
        self._x = 0
        self._vx = max(self._vx, 0)
        self._ax = max(self._ax, 0)

    def hit_right_edge(self, cols):
        self._y = cols - self.__width
        self._vy = min(0, self._vy)
        self._ay = min(0, self._ay)
    
    def move_up(self):
        self._vx -= 2

    def move_left(self):
        self._vy -= 1

    def move_right(self):
        self._vy += 1

