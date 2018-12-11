class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        i = 1
        oldA = A
        while len(A) <= 3 * len(B) or i < 3:
            if B in A:
                return i
            i += 1
            A += oldA
        return -1