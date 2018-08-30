# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        temp = []
        my_list = []
        current = head
        while current:
            temp.append(current.val)
            current = current.next
        for element in temp:
            if temp.count(element) == 1:
                my_list.append(element)
        if not my_list:
            return None
        head = None
        for i in range(len(my_list)):
            if i == 0:
                head = ListNode(my_list[i])
                prev = head
            else:
                node = ListNode(my_list[i])
                prev.next = node
                prev = node
        return head
