# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        previous = head
        current = head.next
        while current:
            if current.val == previous.val:
                previous.next = current.next
                current = current.next
            else:
                previous = current
                current = current.next
        return head
