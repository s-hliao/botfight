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
    PLAYER1_BODY = 3
    PLAYER2_BODY = 4
    PLAYER1_HEAD = 5
    PLAYER2_HEAD = 6
