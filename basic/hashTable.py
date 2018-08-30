class Item:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "%s => %s" % (self.key, self.value)


class HashTable:

    def __init__(self):
        self.capacity = 256
        self.count = 0
        self.slots = [None for i in range(self.capacity)]

    def _hashIt(self, key):
        i = 1
        res = 0
        for c in key:
            res += i * ord(c)
            i += 1
        return res % self.capacity

    def put(self, key, value):
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
        hashValue = self._hashIt(key)
        while self.slots[hashValue] is not None:
            if self.slots[hashValue].key == key:
                return self.slots[hashValue].value
            hashValue = (hashValue + 1) % self.capacity
        return None

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        self.get(key)


if __name__ == "__main__":
    myHashTable = HashTable()
    myHashTable.put("abc", 1)
    myHashTable.put("acd", 2)
    test = myHashTable.get("abc")
    print(test)