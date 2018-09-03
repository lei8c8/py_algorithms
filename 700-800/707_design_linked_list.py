class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index >= self.size:
            return -1
        elif index == 0:
            return self.head.val
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            return current.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = Node(val)
        if self.head is None:
            self.head = node
            self.size = 1
        else:
            node.next = self.head
            self.head = node
            self.size += 1
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        node = Node(val)
        if self.head is None:
            self.head = node
            self.size = 1
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            self.size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index == self.size:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        elif index > self.size:
            return None
        else:
            current = self.head
            prev = self.head
            node = Node(val)
            for _ in range(index):
                prev = current
                current = current.next
            prev.next = node
            node.next = current
            self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if self.size <= 1:
            self.head = None
            self.size = 0
        if index >= self.size:
            return None
        current = self.head
        prev = self.head
        for _ in range(index):
            prev = current
            current = current.next
        prev.next = current.next
        self.size -= 1

    def iter(self):
        current = self.head
        while current:
            value = current.val
            current = current.next
            yield value


if __name__ == "__main__":
    obj = MyLinkedList()
    obj.addAtHead(1)
    obj.addAtHead(2)
    obj.addAtHead(3)
    print("Testing add at head:")
    for element in obj.iter():
        print(element, end = " ")
    print()
    obj.addAtTail(4)
    obj.addAtTail(5)
    obj.addAtTail(6)
    print("Testing add at tail:")
    for element in obj.iter():
        print(element, end = " ")
    print()
    obj.addAtIndex(3, 100)
    print("Testing add at index (3,100):")
    for element in obj.iter():
        print(element, end = " ")
    print()
    obj.addAtIndex(3, 200)
    print("Testing add at index (3,200):")
    for element in obj.iter():
        print(element, end = " ")
    print()
    obj.addAtIndex(8, 88)
    print("Testing add at index (8,88):")
    for element in obj.iter():
        print(element, end = " ")
    print()

    obj.deleteAtIndex(4)
    print("Deleting index 4")
    for element in obj.iter():
        print(element, end = " ")
    print()

    
    obj.deleteAtIndex(40)
    print("Deleting index 40")
    for element in obj.iter():
        print(element, end = " ")
    print()