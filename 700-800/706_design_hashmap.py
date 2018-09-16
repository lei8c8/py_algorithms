
class Item:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "%s => %s" % (self.key, self.value)


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 256
        self.count = 0
        self.slots = [None for i in range(self.capacity)]

    def _hashIt(self, key):
        i = 1
        res = 0
        for c in str(key):
            res += i * ord(c)
            i += 1
        return res % self.capacity
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        item = Item(key, value)
        hashValue = self._hashIt(key)
        while self.slots[hashValue] is not None:
            if self.slots[hashValue].key == key:
                break
            else:
                hashValue = (hashValue + 1) % self.capacity
        if self.slots[hashValue] is None:
            self.count += 1
        self.slots[hashValue] = item
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hashValue = self._hashIt(key)
        while self.slots[hashValue] is not None:
            if self.slots[hashValue].key == key:
                return self.slots[hashValue].value
            hashValue = (hashValue + 1) % self.capacity
        return -1        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        hashValue = self._hashIt(key)
        while self.slots[hashValue] is not None:
            if self.slots[hashValue].key == key:
                self.slots[hashValue] = None
                return
            hashValue = (hashValue + 1) % self.capacity
        return    