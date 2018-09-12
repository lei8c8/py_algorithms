# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from random import randint

class Solution:

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.size = 0
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        count = self._size(self.head)
        random_number = randint(1, count)
        i = 1
        prev = self.head
        current = self.head
        while i <= random_number:
            prev = current
            current = current.next
            i += 1
        return prev.val


    def _size(self, head):
        current = head
        self.size = 0
        while current:
            self.size += 1
            current = current.next
        return self.size