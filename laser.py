from person import GameObject
from colorama import Fore, Back, Style
import numpy as np


class Laser(GameObject):
    def __init__(self, x, y, vx, vy, type_of_laser):
        GameObject.__init__(self, x, y, vx, vy)
        self._active = True
        self.__type = type_of_laser

        if(type_of_laser == 1):
            self._shape = np.full((1, 5), Back.RED + " ")
            self.__height = 1
            self.__width = 5
        elif(type_of_laser == 2):
            self._shape = np.full((5, 1), Back.RED + " ")
            self.__height = 5
            self.__width = 1
        elif(type_of_laser == 3):
            self._shape = np.full((5, 5), Back.BLUE + " ")
            for i in range(5):
                self._shape[i][i] = Back.RED + " "
            self.__height = 5
            self.__width = 5
        elif(type_of_laser == 4):
            self._shape = np.full((5, 5), Back.BLUE + " ")
            for i in range(5):
                self._shape[i][4 - i] = Back.RED + " "
            self.__height = 5
            self.__width = 5

        self._gravity = 0
        self._drag = 0

    def is_active(self):
        return self._active

    def gettype(self):
        return self.__type

    def getheight(self):
        return self.__height

    def getwidth(self):
        return self.__width

    def hit_left_edge(self):
        self._active = False

    def hit_top(self):
        return

    def hit_ground(self, rows):
        return
