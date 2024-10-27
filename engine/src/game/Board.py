import numpy as np
import torch
import copy
from Player import player
from Queue import queue
from Enums import Move, Direction, Cell
from types import StringType
from collections import Iterable


class Board():
    def __init__(self, map):
        self.snake_a = snake()
        self.snake_b = snake()
        self.apple_spawns = Queue(dim=3)
        self.cells = None
        self.load_map(map)
        self.history = []
        self.a_to_play = True
        self.min_player_size = 4
        self.turn_count = 0

    def load_map(self, map):
        self.snake_a.start(map.startA, map.start_size)
        self.snake_b.start(map.startB, map.start_size)

        self.apple_spawns.push(map.apple_spawns)
        self.cells = map.init_board


    def decide_bid(self, bidA, bidB):
        if (bidB > bidA):
            self.a_to_play = True


    # accepts a tuple
    # first value is direction moved:
    # single direction, list of directions, or np.ndarray representing directions
    # second value is amount sacrificed to make moves
    def is_valid_turn(self, turn, a_to_play=self.a_to_play):
        player = snake_a if a_to_play else snake_b

        try:
            if(len(turn!=2)):
                return False

            actions = turn[0]
            sacrifice = turn[1]

            if(player.get_length() - sacrifice < self.min_player_size):
                return False

            if(isinstance(actions, Iterable) and not isinstance(actions, StringType)):
                if(sacrifice  < len(actions-1) * len(actions-1)):
                    return False
                
                head_loc = player.get_head_loc()
                direction = player.get_direction()
                for action in actions:
                    
                    if not player.is_valid_action(action, direction):
                        return False
                    head_loc, direction = player.get_next_loc(action, head_loc, direction)
                    if not self.is_valid_cell(head_loc, a_to_play):
                        return False   
                return True               
            else:
                if not player.is_valid_action(actions, direction):
                    return False
                head_loc, _ = player.get_next_loc(actions)
                return is_valid_cell(head_loc, a_to_play)
        except:
            return False
    


    def is_valid_cell(self, loc, a_to_play):
        if(not self.cell_in_bounds(loc)):
            return False
        if(a_to_play):
            match Cell(cells[head_loc[0]][head_loc[1]]):
                case Cell.WALL:
                    return False
                case Cell.PLAYERB_HEAD:
                    return False
                case Cell.PLAYERB_BODY:
                    return False
        else:
            match Cell(cells[head_loc[0]][head_loc[1]]):
                case Cell.WALL:
                    return False
                case Cell.PLAYERA_HEAD:
                    return False
                case Cell.PLAYERA_BODY:
                    return False
        return True
            
            

    def cell_in_bounds(self, loc):
        return 0 <= loc[0] < self.cells.shape[0] and 0 <= loc[1] < self.cells.shape[1] 

    
                                
    # returns true on full application of all moves if check_validity is on
    # automatically returns true if no checks on
    def apply_turn(self, moves, a_to_play = self.a_to_play, check_validity = True):
        player = snake_a if a_to_play else snake_b

        if(check_validity):
            try:
                if(len(turn!=2)):
                    return False

                actions = turn[0]
                sacrifice = turn[1]

                if(player.get_length() - sacrifice < self.min_player_size):
                    return False

                if(isinstance(actions, Iterable) and not isinstance(actions, StringType)):
                    if(sacrifice  < len(actions-1) * len(actions-1)):
                        return False
                    for action in actions:
                        if not apply_move(action, a_to_play, check_validity=True):
                            return False
                    self.turn_count+=1
                    return True                
                else:
                    valid = apply_move(actions, a_to_play, check_validity=True)   
                    if valid:
                        self.turn_count +=1
                    return valid   
            except:
                return False
        else:
            try:
                actions = turn[0]
                sacrifice = turn[1]

                if(isinstance(actions, Iterable) and not isinstance(actions, StringType)):
                    for action in actions:
                        apply_move(action, a_to_play, check_validity = False)
                    self.turn_count+=1
                else:
                    apply_move(actions, a_to_play, check_validity = False)
                    self.turn_count+=1
                
                return True
            except:
                return False

    def apply_move(self, action, a_to_play = self.a_to_play, check_validity = True):
        head_enum = Cell.PLAYERA_HEAD if self.a_to_play else Cell.PLAYERB_HEAD 
        body_enum = Cell.PLAYERA_BODY if self.a_to_play else Cell.PLAYERB_BODY
        if(check_validity):
            try:
                if not player.is_valid_action(action):
                    return False
                head_loc, _ = player.get_next_loc(action)
                if not self.is_valid_cell(head_loc, a_to_play):
                    return False 
                snake_head, snake_tail = player.push_move(action)
                if(Cell(cells[snake_head]) == Cell.APPLE):
                    player.eat_apple()
                

                return True
            except:
                return False
        else:
            self.cells[player.get_head_loc] = int (body_enum)
            snake_head, snake_tail = player.push_move(action)
            if(Cell(cells[snake_head]) == Cell.APPLE):
                player.eat_apple()
            self.cells[snake_head] = int (head_enum)
            if(snake_tail is not None):
                self.cells[snake_tail] = int (Cell.SPACE)


    def getRoundNum():
        return self.turn_count % 2


    def get_copy(self):
        return copy.deepcopy(self)



