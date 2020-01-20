from person import GameObject
import numpy as np
from colorama import Fore, Back, Style


class Boss(GameObject):

    def __init__(self, x, y, vx, vy):
        GameObject.__init__(self, x, y, vx, vy)
        self.__color = Back.BLUE
        self.shape_string = r"""                     ^    ^
                   / \  //\
     |\___/|      /   \//  .\
     /O  O  \__  /    //  | \ \
    /     /  \/_/    //   |  \  \
    @___@'    \/_   //    |   \   \
       |       \/_ //     |    \    \
       |        \///      |     \     \
      _|_ /   )  //       |      \     _\
     '/,_ _ _/  ( ; -.    |    _ _\.-~        .-~~~^-.
     ,-{        _      `-.|.-~-.           .~         `.
      '/\      /                 ~-. _ .-~      .-~^-.  \
         `.   {            }                   /      \  \
       .----~-.\        \-'                 .~         \  `. \^-.
      ///.----..>    c   \             _ -~             `.  ^-`   ^-_
        ///-._ _ _ _ _ _ _}^ - - - - ~                     ~--,   .-~
"""

        self.shape = self.__getshape()
        (self.height, self.width) = self.shape.shape
        self.gravity = 0
        self.drag = 0
        self.lives = 3

    def hit_ground(self, rows):
        return

    def hit_left_edge(self):
        return

    def hit_top(self):
        return

    def hit_right_edge(self, cols):
        return

    def __getshape(self):
        arr = [[self.__color + char for char in line]
               for line in self.shape_string.split("\n")]
        # pad with spaces
        maxlen = len(max(arr, key=len))
        for i in range(len(arr)):
            if(len(arr[i]) < maxlen):
                arr[i] += [self.__color + " "] * (maxlen - len(arr[i]))
        arr = np.array(arr)
        print(arr.shape)
        return np.array(arr)

    def adjustposition(self, x, rows):
        self.x = x
        if x + self.height >= rows:
            self.x = rows - self.height - 1
        return
