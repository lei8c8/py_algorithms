# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next is None:
            return head
        elif head.next.next is None:
            return head.next
        slow = head 
        fast = head
        while slow.next:
            slow = slow.next
            fast = fast.next.next
            if fast.next is None:
                return slow
            if fast.next.next is None:
                return slow.next