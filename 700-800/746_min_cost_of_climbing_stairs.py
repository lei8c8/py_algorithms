class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-2] + cost[i], dp[i-1] + cost[i])
        return min(dp[-1], dp[-2])

if __name__ == "__main__":
    s = Solution()
    data = [10, 15, 20]
    result = s.minCostClimbingStairs(data)
    print(result)