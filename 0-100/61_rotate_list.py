class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return head
        k = k % self.getLength(head)
        for i in range(k):
            head = self.rotateOnce(head)
        return head

    def getLength(self, head):
        if not head: return 0
        cur = head
        i = 0
        while cur:
            i += 1
            cur = cur.next
        return i

    def rotateOnce(self, head):
        move = head
        for i in range(self.getLength(head) - 2):
            move = move.next
        move.next.next = head
        head = move.next
        move.next = None
        return head