class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        sum = 0
        i = 1
        while sum <= n:
            sum += i
            i += 1
        return i - 2

if __name__ == "__main__":
    solution = Solution()
    result = solution.arrangeCoins(10)
    print(result)