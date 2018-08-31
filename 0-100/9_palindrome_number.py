class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x == 0:
            return True
        return x == int(str(x)[::-1])


if __name__ == "__main__":
    solution = Solution()
    testdata = -121
    result = solution.isPalindrome(testdata)
    print(result)