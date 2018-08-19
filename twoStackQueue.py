class TwoStackQueue:
    def __init__(self):
        self.inStack = []
        self.outStack = []

    def enqueue(self, item):
        self.inStack.append(item)

    def dequeue(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack.pop()