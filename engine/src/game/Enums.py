from enum import Enum, auto



class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Move(Enum):
    LEFT = 0
    FORWARD = 1
    RIGHT = 2

class Cell(Enum):
    SPACE = 0
    WALL = 1
    APPLE = 2
    PLAYERA_BODY = 3
    PLAYERB_BODY = 4
    PLAYERA_HEAD = 5
    PLAYERB_HEAD = 6
