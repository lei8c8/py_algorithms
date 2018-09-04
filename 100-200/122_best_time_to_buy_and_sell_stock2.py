class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        res = 0
        if not prices:
            return res
        low = prices[0]
        high = prices[0]
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i + 1] <= prices[i]:
                i += 1
            low = prices[i]
            while i < len(prices) - 1 and prices[i + 1] >= prices[i] :
                i += 1
            high = prices[i]
            res += high -low
        return res