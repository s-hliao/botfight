from numpy import np

class Map:
    def __init__(self, map_directory):
        self.startA = None
        self.startB = None
        self.start_size = None
        self.apple_spawns = None
        self.dim_x = None
        self.dim_y = Nonw
        self.map_string = map_string
        

    def read_map(self, map_string = self.map_string):
        map_to_play.cells = np.empty((self.dim_x, self.dim_y))
        for char in range(len(map_string)):
            mask = 0b10000000
            for i in range(8):
                if (count >= map_to_play.dim_x * map_to_play.dim_y):
                    break
                map_to_play.cells[count / map_to_play.dim_y][count % map_to_play.dim_y] = to_int & mask
                mask >= 1
                count+= 1

        return cells