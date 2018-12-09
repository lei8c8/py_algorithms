class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
        return ''.join(s)