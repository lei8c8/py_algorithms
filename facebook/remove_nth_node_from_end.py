class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None: return head
        left = right = head
        for _ in range(n): 
            right = right.next
        if right is None: 
            return head.next
        while right.next is not None:
            right = right.next
            left = left.next
        left.next = left.next.next
        return head
