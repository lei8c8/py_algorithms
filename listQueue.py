class ListQueue:
    def __init__(self):
        self.items = []
        self.count = 0

    def enqueue(self, item):
        self.items.insert(0, item)
        self.count += 1

    def dequee(self):
        if self.count == 0:
            return None
        else:
            data = self.items.pop()
            self.count -= 1
            return data

    def size(self):
        return self.count
        