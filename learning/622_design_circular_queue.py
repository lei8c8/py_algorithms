class MyCircularQueue:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.size = k
        self.items = [None] * self.size
        self.head = -1 
        self.tail = -1
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 0
            self.tail = 0
            self.items[0] = value
            return True
        if self.tail == self.size - 1:
            self.items[0] = value
            self.tail = 0
            return True
        else:
            self.tail += 1
            self.items[self.tail] = value
            return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        if self.tail == self.head:
            self.items[self.head] = None
            self.tail = -1
            self.head = -1
            return True
        else:
            if self.head == self.size - 1:
                self.items[self.head] = None
                self.head = 0
            else:
                self.items[self.head] = None
                self.head += 1
            return True
        

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.items[self.head]
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.items[self.tail]
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if self.head == -1 and self.tail == -1:
            return True
        return False
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if self.tail - self.head + 1 == self.size or self.head - self.tail == 1:
            return True
        return False