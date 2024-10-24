import numpy as np

class CoordinateQueue:
    #implements a circular queue in numpy
    def __init__(self, init_capacity = 10):
        self.q = np.zeros((init_capacity, 2))
        self.size = 0
        self.capacity = init_capacity
        self.head = 0
        self.tail = 0


    # enqueues x, y as a single coordinate into the numpy array
    def push(self, x, y):
        if(size+1 >= capacity):
            self.resize()
        self.tail = (self.tail+1) % self.capacity
        self.q[self.tail] = np.array([x, y])
        self.size += 1 


    #enqueues a 2-value move into the queue
    def push(self, move):
        if(size+1 >= capacity):
            self.resize()
        self.tail = (self.tail+1) % self.capacity
        self.q[self.tail, :] = move
        self.size += 1 


    def pop(self):
        data = self.q[self.head]
        self.head = (self.head+1) % self.capacity
        self.size -= 1
        return data

    def resize(self):
        new_array = np.zeros((self.capacity * 2, 2))
        new_array[0:size, :] = self.q[np.arange(self.head, self.tail) % self.capacity, : ]
        self.capacity = self.capacity *2
        self.head = 0
        self.tail = self.size-1


