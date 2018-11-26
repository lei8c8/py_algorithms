from collections import Counter

class Solution:
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        ans = 0
        for i in range(1, len(A)):
            if A[i] <=  A[i-1]:
                ans += (A[i-1] - A[i] + 1)
                A[i] = A[i-1] + 1
        return ans