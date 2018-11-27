class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if len(A) <= 1: return 0
        minVal = maxVal = A[0]
        for i in range(1, len(A)):
            if A[i] < minVal: minVal = A[i]
            if A[i] > maxVal: maxVal = A[i]
        if maxVal - minVal <= 2 * K: return 0
        return maxVal - minVal - 2 * K 