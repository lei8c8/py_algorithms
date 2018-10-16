class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        length = len(A)
        res = [None] * length
        j, k = 0, 1
        for i in range(length):
            if A[i] % 2 == 0:
                res[j] = A[i]
                j += 2
            else:
                res[k] = A[i]
                k += 2
        return res
