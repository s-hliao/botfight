class game_map:
    def __init__(self, map_directory):
        self.startA = None
        self.startB = None
        self.start_size = None
        self.apple_spawns = None

    def read_map(self):
        return