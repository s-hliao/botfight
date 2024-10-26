import numpy as np
import torch
import copy
from Player import player
from Queue import queue

class Board():
    def __init__(self, map):
        self.player_a = Player()
        self.player_b = Player()
        self.apple_spawns = Queue(dim=3)
        self.load_map(map)
        self.history = []
        

    def load_map(self, map):
        self.player_a.start(map.startA, np.start_size)
        self.player_b.start(map.startB, np.start_size)

        self.apple_spawns.push(map.apple_spawns)
        self.cells = map.init_board

    # def enum 0 is space, 1 is wall, 2 is apple, 3 is player 1 body, 4 is player 2 body, 5 is player 1 head, 6 is player 2 head
    # return 
    def a_move(self, move):
        if

    def b_move(self, moves):

    def get_copy(self):
        return copy.deepcopy(self)



