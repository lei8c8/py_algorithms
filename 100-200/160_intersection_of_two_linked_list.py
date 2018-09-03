# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        pointer_A = headA
        pointer_B = headB
        counter_A = 0
        counter_B = 0
        while True:
            if pointer_A == pointer_B:
                return pointer_A
            pointer_A = pointer_A.next
            pointer_B = pointer_B.next
            if pointer_A is None:
                pointer_A = headB
                counter_A += 1
            if pointer_B is None:
                pointer_B = headA
                counter_B += 1
            if counter_A > 1 or counter_B > 1:
                break
        return None