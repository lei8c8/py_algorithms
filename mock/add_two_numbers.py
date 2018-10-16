# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        two_sum = int(self.get_number(l1)) + int(self.get_number(l2))
        return self.construct_list(two_sum)


    def get_number(self, node):
        current = node 
        result = []
        while current:
            result.append(str(current.val))
            current = current.next
        return ''.join(result[::-1])

    def construct_list(self, number):
        number_str = str(number)[::-1]
        head = ListNode(int(number_str[0]))
        current = head
        for i in range(1, len(number_str)):
            node = ListNode(int(number_str[i]))
            current.next = node
            current = current.next
        return head