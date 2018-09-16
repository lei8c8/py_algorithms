class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 1000001
        self.items = [None] * self.capacity
        

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.items[key] = key
        

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.items[key] = None

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return not self.items[key] == None
        
