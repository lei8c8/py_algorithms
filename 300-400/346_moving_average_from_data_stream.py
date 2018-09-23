from collections import deque

class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.count = 0
        self.queue = deque([], maxlen=self.size)
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.queue.append(val)
        self.count += 1
        if self.count <= self.size:
            return sum(self.queue) / self.count
        else:
            return sum(self.queue) / self.size 