from collections import deque

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = deque([])
        self.size = 0

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.items.append(x)
        self.size += 1
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        res = self.items[-1]
        self.items.pop()
        self.size -= 1
        return res

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.items[-1]
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.items) == 0
        
