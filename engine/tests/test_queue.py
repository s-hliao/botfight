import pytest
from src.game.game_queue import Queue
import numpy as np


def test_push():
    q = Queue(dim=1)
    q.push(0)
    assert q.peek_head() == 0
    assert q.peek_tail() == 0
    assert q.head == 0
    assert q.tail == 0

    for i in range(1, 100):
        q.push(i)
        assert q.peek_head() == 0
        assert q.peek_tail() == i

        assert q.head == 0
        assert q.tail == i

def test_pop():
    q = Queue(dim=1)
    for i in range(0, 100):
        q.push(i)

    for i in range(0, 100):
        assert q.peek_head() == i
        assert q.pop() == i
        
        assert q.peek_tail() == 99

def test_pushpop():
    q = Queue(dim=1)
    for i in range(0, 25):
        q.push(i)
        assert q.peek_tail() == i

    for i in range(0, 25):
        assert q.pop() == i

    for i in range(25, 50):
        q.push(i)
        assert q.peek_tail() == i

    for i in range(25, 50):
        assert q.pop() == i

    for i in range(50, 70):
        q.push(i)
        assert q.peek_tail() == i

    for i in range(50, 60):
        assert q.pop() == i

    for i in range(70, 90):
        q.push(i)
        assert q.peek_tail() == i

    for i in range(60, 70):
        assert q.pop() == i

    for i in range(90, 100):
        q.push(i)
        assert q.peek_tail() == i

    for i in range(70, 100):
        assert q.pop() == i


def test_push_many():
    q = Queue(dim=1)
    for i in range(0, 10):
        q.push_many(np.arange(i*10, (i+1)*10))
        
        assert q.peek_head() == 0
        assert q.peek_tail() == ((i+1)*10)-1

        assert q.head == 0
        assert q.tail == ((i+1)*10)-1
    assert q.size == 100

def test_pop_many():
    q = Queue(dim=1)
    for i in range(0, 10):
        q.push_many(np.arange(i*10, (i+1)*10))
    
    for i in range(0, 10):
        arr = q.pop_many(10)
        assert np.allclose(arr, np.arange(i*10, (i+1)*10).reshape(-1,1))
        
    assert q.size == 0
    

def test_push_pop_many():
    q = Queue(dim=1)
    
    q.push_many(np.arange(0, 50))
    assert q.size == 50
    assert q.peek_head() == 0
    assert q.peek_tail() == 49


    assert np.allclose(q.pop_many(25), np.arange(0, 25).reshape(-1,1))
    q.push_many(np.arange(50, 100))
    assert q.peek_head() == 25
    assert q.peek_tail() == 99
    assert q.size == 75
    assert np.allclose(q.pop_many(25), np.arange(25, 50).reshape(-1,1))
    
    assert q.size == 50
    assert np.allclose(q.pop_many(50), np.arange(50, 100).reshape(-1,1))
    assert q.size == 0

def test_push_pop_dim():
    q = Queue(dim=2)
    for i in range (0, 50):
        q.push(np.array([2*i, 2*i +1]).reshape(-1, 2))

    for i in range(0, 50):
        assert np.allclose(q.pop(), np.array([2*i, 2*i +1]).reshape(-1, 2))