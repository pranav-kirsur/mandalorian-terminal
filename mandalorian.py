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
        self.height = 3
        self.width = 3
        self.gravity = 0.115
        self.drag = 0.05
        self.coins_collected = 0
        self.lives = 3
        self.shield_active = False

    def hit_ground(self, rows):
        self.x = rows - self.height
        self.vx = min(0, self.vx)
        self.ax = min(0, self.ax)

    def hit_left_edge(self):
        self.y = 0
        self.vy = max(0, self.vy)
        self.ay = max(0, self.ay)

    def hit_top(self):
        self.x = 0
        self.vx = max(self.vx, 0)
        self.ax = max(self.ax, 0)

    def hit_right_edge(self, cols):
        self.y = cols - self.width
        self.vy = min(0, self.vy)
        self.ay = min(0, self.ay)
