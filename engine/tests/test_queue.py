import pytest
from queue import Queue


def test_push():
    q = Queue(dim = 1)
    q.push(0)
    assert q.peek_head() == 0
    assert q.peek_tail() == 0

    for i in range(2, 100):
        assert q.peek_head() == 0
        assert q.peek_tail() == i
        assert q.peek_many() == np.arange(i)

    