from Queue import queue
from Enums import Direction

class snake:
    def __init__(self, min_player_size=4):
        self.q = queue()
        self.direction = None
        self.apples_queued = 0
        self.apples_eaten = 0
        self.min_player_size = min_player_size
        

    def start(self, start_loc, start_size):
        blocks.push(start_loc)
        apples_queued = start_size - 1
        
    def get_head_loc(self):
        return q.peek_head()

    def get_tail_loc(self):
        return q.peek_tail()

    def get_all_loc(self):
        return q.peek_all()

    def get_direction(self):
        return self.direction


    def get_length(self):
        return self.q.size + apples_queued

    def get_next_loc(self, action, head_loc=self.get_head_loc(), move_dir = self.direction):

        move_dir = Direction(action)
      
        match move_dir:
            case Direction.NORTH:
                head_loc[1]-=1
            case Direction.EAST:
                head_loc[0]+=1
            case Direction.SOUTH:
                head_loc[1]+=1
            case direction.WEST:
                head_loc[0]-=1
            case _:
                return None

        return head_loc, move_dir
    
    

    def is_valid_bid(self, bid):
        return self.get_length() - bid > self.min_player_size 


    def is_valid_action(self, move, dir):
        return 0 < int(move) < 4 and (self.direction is None or (int(dir) + 2) % 4 is not int(move))

    def get_valid_actions(self, direction = self.direction):
        x = int (self.direction)
        return [Direction((x-1+4)%4), self.direction,  Direction((x+1)%4)]


    def eat_apple(self):
        self.apples_queued += 1
        self.apples_eaten += 1

    def get_apples_eaten(self):
        return self.apples_eaten

    def apply_bid(self, bid):
        self.apples_queued -= bid

    def push_move(self, action):
        head_loc = self.get_head_loc()

        match action:
            case Direction.NORTH:
                head_loc[1]-=1
            case Direction.EAST:
                head_loc[0]+=1
            case Direction.SOUTH:
                head_loc[1]+=1
            case direction.WEST:
                head_loc[0]-=1
            case _:
                return None

        self.q.push(head_loc)

        snake_tail = None
        if(self.apples_queued == 0):
            snake_tail = self.q.pop()  
        else:
            self.apples_queued-=1
        
        return snake_head, snake_tail