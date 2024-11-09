import pytorch as torch
from game.Enums import Direction
class PlayerController:
    # for the controller to read
    def __init__(self):
        self.usesGPU = False

    def init_player(self, tensor:torch.tensor):
        return

    def bid(self, board:Board):
        return 0

    def play(self, board:Board, time_left):
        return ([Direction.EAST], 0)