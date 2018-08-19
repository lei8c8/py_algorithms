class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    
    def __str__(self):
        return self.data

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.count += 1

    def pop(self):
        if not self.top:
            return None
        else:
            data = self.top.data
            self.top = self.top.next
            self.count -= 1
            return data

    def peek(self):
        if not self.top:
            return None
        else: 
            return self.top.data

    def size(self):
        return self.count