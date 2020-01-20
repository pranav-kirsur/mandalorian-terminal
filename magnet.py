from person import GameObject
from colorama import Fore, Back, Style
import numpy as np


class Magnet(GameObject):
    def __init__(self, x, y, vx, vy):
        GameObject.__init__(self, x, y, vx, vy)
        self.is_active = True
        self.height = 1
        self.width = 1
        self.shape = np.array([[Back.BLACK + 'M']])
        self.gravity = 0
        self.drag = 0

    def hit_left_edge(self):
        self.is_active = False

    def collect(self):
        self.is_active = False

    def hit_top(self):
        return

    def hit_ground(self, rows):
        return

    def attract(self, player):
        if(abs(player.x - self.x) < 50 and abs(player.y - self.y) < 50):
            player.vx += 0.05 * (self.x - player.x)
            player.vy += 0.05 * (self.y - player.y)
