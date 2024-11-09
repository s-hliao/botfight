import numpy as np

class Queue:
    #implements a circular queue in numpy
    def __init__(self, dim=2, init_capacity = 10):
        self.q = np.zeros((init_capacity, dim))
        self.size = 0
        self.dim=dim
        self.capacity = init_capacity
        self.head = 0
        self.tail = 0


    #enqueues a 2-value move into the queue
    def push(self, move):
        if(self.size+1 >= self.capacity):
            new_array = np.zeros((self.capacity * 2, self.dim))
            new_array[0:self.size, :] = self.q[np.arange(self.head, self.tail+1) % self.capacity, : ]
            self.capacity = self.capacity *2
            self.head = 0
            self.tail = self.size
            if(self.size!=0):
                self.tail = self.size-1
            self.q = new_array

        if(self.size != 0):
            self.tail = (self.tail+1) % self.capacity
        self.q[self.tail, :] = move
        self.size += 1 
    
    def peek_head(self):
        return self.q[self.head]

    def peek_tail(self):
        return self.q[self.tail]

    def peek_all(self):
        return self.q[np.arange(self.head, self.tail) % self.capacity, : ]

    def push_many(self, moves):
        if(self.size+len(moves) >= self.capacity):
            new_array = np.zeros(((self.capacity +len(moves))* 2, self.dim))
            new_array[0:self.size, :] = self.q[np.arange(self.head, self.tail+1) % self.capacity, : ]
            self.capacity = (self.capacity +len(moves))* 2
            self.head = 0
            self.tail = self.size
            if(self.size!=0):
                self.tail -= 1
            self.q = new_array

        if(self.size!=0):
            self.tail = (self.tail+1) % self.capacity
        
        self.q[np.arange(self.tail, self.tail+len(moves)) % self.capacity, :] = moves.reshape(-1, self.dim)
        self.tail = (self.tail+len(moves)-1) % self.capacity
        self.size += len(moves)

    def pop(self):
        if(self.size==0):
            raise IndexError("Popped on empty Queue")
        
        data = self.q[self.head]
        if(self.size != 1):
           self.head = (self.head+1) % self.capacity
        self.size -= 1
        return data

    def pop_many(self, num_moves):
        if(self.size-num_moves < 0):
            raise IndexError("Popped too many elements from Queue")
        data = self.q[self.head:self.head+num_moves,:]
        self.head = (self.head+num_moves) % self.capacity
        self.size -= num_moves
        return data
        


