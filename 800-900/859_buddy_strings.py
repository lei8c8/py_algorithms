class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B): return False
        length = len(A)
        newListA, newListB = [], []
        # ignore the same element
        for i in range(length):
            if A[i] != B[i]:
                newListA.append(A[i])
                newListB.append(B[i])
        if (len(newListA) == 0 and len(A) == len(set(A))) or (len(newListA) == 1 or len(newListA) > 2):
            return False
        if newListA[::-1] != newListB:
            return False
        return True