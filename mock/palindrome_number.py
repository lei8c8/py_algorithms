class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return list(str(x)) == list(str(x))[::-1]