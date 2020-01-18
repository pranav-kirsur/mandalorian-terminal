from person import GameObject
import numpy as np
from colorama import Fore, Back, Style


class Bullet(GameObject):
    def __init__(self, x, y, vx, vy):
        GameObject.__init__(self, x, y, vx, vy)

        self.shape = np.full((1, 2), Back.MAGENTA + " ")
        self.height = 1
        self.width = 2
        self.is_active = True
        self.gravity = 0
        self.drag = 0

    def hit_left_edge(self):
        self.is_active = False
    
    def hit_right_edge(self, cols):
        self.is_active = False

    def hit_top(self):
        return
    
    def hit_ground(self, rows):
        return
