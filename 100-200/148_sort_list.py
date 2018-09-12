# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        current = head
        my_list = []
        while current:
            my_list.append(current.val)
            current = current.next
        my_list.sort()
        print(my_list)
        list_len = len(my_list)
        i = list_len - 1
        prev = None
        while i >= 0:
            node = ListNode(my_list[i])
            if i == list_len:
                head = node
                prev = node 
            else:
                node.next = prev
                prev = node 
            i -= 1
        return prev