class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        save_pairs = []
        current = head
        while current and current.next:
            next_head = current.next.next
            new_head = current.next
            new_head.next = current
            current = next_head
            save_pairs.append((new_head, new_head.next))
        if current:
            save_pairs.append((current,))
        for i in range(len(save_pairs) - 1):
            (save_pairs[i][1]).next = save_pairs[i+1][0]
        if len(save_pairs[-1]) == 1:
            (save_pairs[-1][0]).next = None
        else:
            (save_pairs[-1][-1]).next = None
        return save_pairs[0][0]