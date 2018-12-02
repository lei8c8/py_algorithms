class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def helper(x, n):
            if n == 0: return 1.0
            h = helper(x, n // 2)
            if (n % 2 == 0): return h * h
            else: return h * h * x
        if n >= 0:
            return helper(x, n)
        return 1 / helper(x, -n)