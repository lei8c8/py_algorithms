from collections import deque

class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B:
            return True
        aDeque, bDeque = deque(A), deque(B)
        for _ in range(len(A)):
            aDeque.append(aDeque.popleft())
            if aDeque == bDeque:
                return True
        return False