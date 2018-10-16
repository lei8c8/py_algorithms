# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1: return l2
        if not l2: return l1
        if not l1 and not l2: return None
        ahead_head = ListNode(-1)
        res = ahead_head
        while l1 and l2:
            if l1.val > l2.val: 
                res.next = l2
                l2 = l2.next 
                res = res.next
            else:
                res.next = l1
                l1 = l1.next
                res = res.next
        if l1 is None:
            res.next = l2
        if l2 is None:
            res.next = l1
        head = ahead_head.next
        return head
                
        