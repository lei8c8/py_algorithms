# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        elif head.next is None or head.next.next is None:
            return head
        odd_current = head
        even_current = head.next
        while odd_current.next and even_current.next:
            odd_current.next = even_current.next
            even_current.next = odd_current.next.next
            odd_current = odd_current.next
            even_current = even_current.next
        odd_current.next = head.next
        return head

