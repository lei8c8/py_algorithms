class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        if len(prices) < 2:
            return max_profit
        min_price = prices[0]
        for price in prices:
            if price < min_price:
                min_price = price
            if price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
            
if __name__ == "__main__":
    solution = Solution()
    testdata = []
    result = solution.maxProfit(testdata)
    print(result)