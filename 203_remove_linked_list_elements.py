# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # Check if head is None
        if not head:
            return None
        # Check whether value of head == val
        while head and head.val == val:
            head = head.next
        # Check if head is None again
        if not head:
            return None
        previous = head
        current = head.next
        while current:
            if current.val == val:
                if current.next:
                    previous.next = current.next
                    privous = current
                    current = current.next
                else:
                    previous.next = None
                    current = None
                    break
            else:
                previous = current
                current = current.next
        return head