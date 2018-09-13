# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        lookup = set(G)
        current = head
        res = 0
        while current:
            if current.val in lookup and (current.next.val not in lookup or current.next is None):
                res += 1
            current = current.next
        return res