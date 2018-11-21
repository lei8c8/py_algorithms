class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """    
        prevPrev, prev  = cost[0], cost[1]
        for i in range(2, len(cost)):
            cur = min(prevPrev, prev) + cost[i]
            prevPrev, prev = prev, cur
        return min(prevPrev, prev)

if __name__ == "__main__":
    s = Solution()
    data = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    result = s.minCostClimbingStairs(data)
    print(result)