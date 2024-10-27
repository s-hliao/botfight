import pytorch as torch
class Controller:
    # for the controller to read
    def __init__(self):
        self.usesGPU = False

    def init_player(self, tensor:torch.tensor):
        return

    def bid(self, board:Board):
        return 0

    def run(self, board:Board):
        return ([], 0)