from person import Person
import numpy as np


class Mandalorian(Person):

    def __init__(self, x, y):
        Person.__init__(self, x, y)
        self.shape = np.array([['/','O','\\'],['-','-','-'],['-','-','-']])
        self.height = 3
        self.width = 3