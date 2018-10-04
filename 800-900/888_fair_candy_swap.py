class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sumA, sumB = sum(A), sum(B)
        setB = set(B)
        diff = (sumB - sumA) // 2
        for element in A:
            if diff + element in setB:
                return [element, diff + element]