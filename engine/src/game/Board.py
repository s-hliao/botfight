import numpy as np


class Board():
    def __init__(self, dim_x, dim_y):
        self.dim_x = dim_x
        self.dim_y = dim_y
        self.cells = np.zeros((dim_x, dim_y))
        self.PlayerA = Queue()
        self.PlayerB = Queue()


    def load_map():
        