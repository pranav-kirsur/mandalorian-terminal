from person import GameObject
from colorama import Fore, Back, Style
import numpy as np


class Magnet(GameObject):
    def __init__(self, x, y, vx, vy):
        GameObject.__init__(self, x, y, vx, vy)
        self.is_active = True
        self.__height = 1
        self.__width = 1
        self._shape = np.array([[Back.BLACK + 'M']])
        self._gravity = 0
        self._drag = 0

    def getheight(self):
        return self.__height
    
    def getwidth(self):
        return self.__width

    def hit_left_edge(self):
        self.is_active = False

    def collect(self):
        self.is_active = False

    def hit_top(self):
        return

    def hit_ground(self, rows):
        return

    def attract(self, player):
        if(abs(player.getx() - self._x) < 50 and abs(player.gety() - self._y) < 50):
            player.setvx(player.getvx() + 0.05 * (self._x - player.getx()))
            player.setvy(player.getvy() + 0.05 * (self._y - player.gety()))
