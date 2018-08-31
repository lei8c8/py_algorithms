# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        list1 = self.traversalList(head)
        reversed_head = self.reverseList(head)
        list2 = self.traversalList(reversed_head)
        return list1 == list2
    
    def reverseList(self, head):
        if not head:
            return None
        if not head.next:
            return head
        current = head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    
    def traversalList(self, head):
        res = []
        if not head:
            return None
        current = head
        while current:
            res.append(current.val)
            current = current.next
        return res       