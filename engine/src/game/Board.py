import numpy as np
import torch
import copy
from Player import player
from Queue import queue

from types import StringType
from collections import Iterable


class Board():
    def __init__(self, map):
        self.player_a = Player()
        self.player_b = Player()
        self.apple_spawns = Queue(dim=3)
        self.load_map(map)
        self.history = []
        self.a_to_play = True

    def load_map(self, map):
        self.player_a.start(map.startA, np.start_size)
        self.player_b.start(map.startB, np.start_size)

        self.apple_spawns.push(map.apple_spawns)
        self.cells = map.init_board

    # accepts a tuple
    # first value is direction moved:
    # single direction, list of directions, or np.ndarray representing directions
    # second value is amount sacrificed to make moves
    def is_valid_move(self, move, a_to_play=self.a_to_play):
        try:
            if(len(move!=2)):
                return False

            actions = move[0]
            sacrifice = move[1]
            if(isinstance(actions, Iterable) and not isinstance(actions, StringType)):
                if(sacrifice  < len(actions) * len(actions)):
                    return False
                if(a_to_play):
                    
                else:
            else:
                if(a_to_play):

                else:
        catch:
            return False
                
            


    def a_move(self, moves):
        if len(a_move) > 0:


    def b_move(self, moves):

    def get_copy(self):
        return copy.deepcopy(self)



