from person import GameObject
from colorama import Fore, Back, Style
import numpy as np


class Laser(GameObject):
    def __init__(self, x, y, vx, vy, type_of_laser):
        GameObject.__init__(self, x, y, vx, vy)
        self.is_active = True
        self.type = type_of_laser

        if(type_of_laser == 1):
            self.shape = np.full((1, 5), Back.RED + " ")
            self.height = 1
            self.width = 5
        elif(type_of_laser == 2):
            self.shape = np.full((5, 1), Back.RED + " ")
            self.height = 5
            self.width = 1
        elif(type_of_laser == 3):
            self.shape = np.full((5, 5), Back.BLUE + " ")
            for i in range(5):
                self.shape[i][i] = Back.RED + " "
            self.height = 5
            self.width = 5
        elif(type_of_laser == 4):
            self.shape = np.full((5, 5), Back.BLUE + " ")
            for i in range(5):
                self.shape[i][4 - i] = Back.RED + " "
            self.height = 5
            self.width = 5

        self.gravity = 0
        self.drag = 0

    def hit_left_edge(self):
        self.is_active = 0

    def collect(self):
        self.is_active = False
