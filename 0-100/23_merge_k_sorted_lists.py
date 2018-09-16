# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        all_values = []
        for i in range(len(lists)):
            current =lists[i]
            if not current:
                continue
            while current:
                all_values.append(current.val)
                current = current.next
        all_values.sort()
        if len(all_values) == 0:
            return []
        prev = ListNode(-1)
        ahead = prev
        for value in all_values:
            node = ListNode(value)
            prev.next = node
            prev = node
        head = ahead.next
        ahead.next = None
        return head
        