# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Given linked list: 1->2->3->4->5, and n = 2.

#After removing the second node from the end, the linked list becomes 1->2->3->5.

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if (head is None) or (head.next is None and n == 1):
            return None
        ahead = head
        behind = head
        try:
            for _ in range(n):
                ahead = ahead.next
        except:
            return None
        if ahead is None:
            head = head.next
            return head
        while ahead.next is not None:
            ahead = ahead.next
            behind = behind.next
        behind.next = behind.next.next
        return head