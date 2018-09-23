# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head = self.reverseList(head)
        current = head 
        while current:
            current.val = current.val + 1
            if current.val != 10:
                break
            else:
                current.val = 0
                if current.next:
                    current = current.next
                else:
                    node = ListNode(1)
                    current.next = node
                    break
        head = self.reverseList(head)
        return head

    def reverseList(self, head):
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
        return prev        