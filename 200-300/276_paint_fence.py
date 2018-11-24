class Solution:
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0: return 0
        if n == 1: return k # you can select any color
        if n == 2: return k ** 2 # you can select any color for both fences
        dp = [0] * (n + 1)
        dp[1], dp[2] = k, k * k
        # if paiting the same color as previous fence
        # dp[i] = diff_ways[i-1] * 1 = dp[i-2] * (k-1)
        # if painting the difference color as previous fence
        # dp[i] = dp[i-1] * (k - 1)
        for i in range(3, n + 1):
            dp[i] = (dp[i-1] + dp[i-2]) * (k-1)
        return dp[-1]
        