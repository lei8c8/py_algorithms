class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.size = 0
        self.smallest = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.size == 0:
            self.items.append(x)
            self.smallest = x
        else:
            self.items.append(x)
            if x < self.smallest:
                self.smallest = x
        self.size += 1
        
        

    def pop(self):
        """
        :rtype: void
        """
        if self.size == 0:
            try:
                self.items.pop()
            except IndexError:
                print("You can't pop() from empty stack.")
        else:
            val = self.items.pop()
            self.size -= 1
            if val == self.smallest and self.size >= 1:
                self.smallest = min(self.items)
            elif val == self.smallest and self.size == 0:
                self.smallest = 0

        
        

    def top(self):
        """
        :rtype: int
        """
        if self.size == 0:
            try:
                _ = self.items[-1]
            except:
                print("It's an empty stack, no value returned.")
                return None
        else:
            return self.items[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.size == 0:
            return None
        else:
            return self.smallest