class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        length = len(A)
        lookup, res = {}, 0
        for i in range(length):
            for j in range(length):
                if A[i] + B[j] not in lookup:
                    lookup[A[i] + B[j]] = 1
                else:
                    lookup[A[i] + B[j]] += 1
        for i in range(length):
            for j in range(length):
                if -(C[i] + D[j]) in lookup:
                    res += lookup[-(C[i] + D[j])]
        return res