class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        moveA, moveB = headA, headB
        counterA, counterB = 0, 0
        while True:
            if moveA == moveB: return moveA
            moveA = moveA.next
            moveB = moveB.next
            if moveA is None: 
                moveA = headB
                counterA += 1
            if moveB is None: 
                moveB = headA
                counterB += 1
            if counterA > 1 or counterB > 1:
                return None