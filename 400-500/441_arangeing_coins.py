class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((-1 + (1 + 8 *n) ** 0.5) / 2)



if __name__ == "__main__":
    solution = Solution()
    result = solution.arrangeCoins(1)
    print(result)