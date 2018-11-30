class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head: return None
        current = head
        previous = ListNode(-1)
        headOfHead = previous
        tmp = []
        while current:
            if current.val >= x:
                tmp.append(current)
                previous.next = current.next
                current = current.next
            else:
                previous.next = current
                previous = current
                current = current.next
        if (len(tmp)) == 0:
            return head
        for i in range(len(tmp)):
            previous.next = tmp[i]
            previous = tmp[i]
        previous.next = None
        return headOfHead.next

