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




    