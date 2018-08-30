from random import randint

class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return self.data


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        node = Node(data, None, None)
        if not self.tail:
            self.head = node
            self.tail = self.head
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.count += 1

    def size(self):
        return self.count

    def delete(self, data):
        nodeDeleted = False
        current = self.head
        if current is None:
            nodeDeleted = False
        # the node to be deleted is the head
        if current.data == data: 
            self.head = current.next
            self.head.prev = None
            nodeDeleted = True
        # the node to be deleted is the tail
        if self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            nodeDeleted = True
        # the node to be deleted is in the middle
        else:
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    nodeDeleted = True
                current = current.next
        # return value to identify whether the deletion is successful
        if nodeDeleted:
            self.count -= 1
        return nodeDeleted

    def iter(self):
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value
    
    def contain(self, data):
        find = False
        for n in self.iter():
            if n == data:
                find = True
                return find
        return find

    def clear(self):
        self.head = None
        self.tail = None
        self.count = 0


