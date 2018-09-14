class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        if m != 1:
            left = head
            left_prev = head
            for _ in range(m - 1):
                left_prev = left
                left = left.next
            right = left
            right_prev = left
            for _ in range(n - m + 1):
                right_prev = right
                right = right.next
            right_prev.next = None
            inner_head, inner_tail = self.reserseList(left)
            left_prev.next = inner_head
            inner_tail.next = right
        else:
            p = head 
            v = head
            for _ in range(n):
                v = p
                p = p.next
            v.next = None
            head, tail = self.reserseList(head)
            tail.next = p

        return head
    
    def reserseList(self, head):
        if not head:
            return
        if not head.next:
            return head
        current = head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev, head       
        