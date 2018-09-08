class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n
        for operation in ops:
            m = min(m, operation[0])
            n = min(n, operation[1])
        return m * n

if __name__ == "__main__":
    solution = Solution()
    result = solution.maxCount(39999, 39999, [[19999,19999]])
    print(result)