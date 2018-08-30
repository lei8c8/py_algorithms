class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.count += 1 

    def size(self):
        return self.count

    def iter(self):
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value

    def search(self, data):
        for node in self.iter():
            if node == data:
                return True
        return False

    def delete(self, data):
        current = self.head
        previous = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = self.head.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next
        return False

    def clear(self):
        self.head = None
        self.tail = None
        self.count = 0

if __name__ == '__main__':
    singlyLinkedList = SinglyLinkedList()
    singlyLinkedList.append('A')
    singlyLinkedList.append('B')
    singlyLinkedList.append('C')
    # test append method
    print("After adding A B C, the singly linked list is:", end = ' ')
    for n in singlyLinkedList.iter():
        print(n, end = ' ')
    print()

    # test size() method
    print("The size of it is: " + str(singlyLinkedList.size()), end = ' ')
    print()

    # test search method
    print("Searching D in the singly linked list: ", singlyLinkedList.search('D'))
    print("Searching B in the singly linked list: ", singlyLinkedList.search('B'))

    # test delete method
    singlyLinkedList.delete('B')
    print("After deleting B: the singly linked list is:", end = ' ')
    for n in singlyLinkedList.iter():
        print(n, end = ' ')
    print()

    # test clear method
    singlyLinkedList.clear()
    print(singlyLinkedList.size(), singlyLinkedList.head, singlyLinkedList.tail)