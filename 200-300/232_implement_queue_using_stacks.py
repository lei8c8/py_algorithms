class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack = []
        self.out_stack = []
        self.size = 0
        
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.in_stack.append(x)
        self.size += 1
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.out_stack) == 0:
            while len(self.in_stack) > 0:
                temp = self.in_stack.pop()
                self.out_stack.append(temp)
        res = self.out_stack.pop()
        self.size -= 1
        return res
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.out_stack) == 0:
            while len(self.in_stack) > 0:
                temp = self.in_stack.pop()
                self.out_stack.append(temp)
        return self.out_stack[-1]        
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.size == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()