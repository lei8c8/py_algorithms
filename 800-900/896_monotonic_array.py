class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3 or len(set(A)) == 1:
            return True
        if A[-1] > A[0]:
            increase = True
        else:
            increase = False
        for i in range(len(A) - 1):
            if increase:
                if A[i+1] < A[i]:
                    return False
            else:
                if A[i+1] > A[i]:
                    return False
        return True

        