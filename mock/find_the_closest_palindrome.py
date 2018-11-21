class Solution:
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        left = int(n) - 1
        right = int(n) + 1
        while True:
            if str(left) == str(left)[::-1]:
                return str(left)
            if str(right) == str(right)[::-1]:
                return str(right)
            left -= 1
            right += 1

if __name__ == "__main__":
    sol = Solution()
    testdata = "123"
    result = sol.nearestPalindromic(testdata)
    print(result)