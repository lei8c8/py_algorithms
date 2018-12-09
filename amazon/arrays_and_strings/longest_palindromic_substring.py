class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start, stop, length = 0, 0, 0
        if len(s) == 0: return ""
        for i in range(len(s)):
            value1 = self.expandFromCenter(s, i, i) # odd scenario
            value2 = self.expandFromCenter(s, i, i + 1) # even scenario
            length = max(value1, value2)
            if length > stop - start:
                start = i - (length - 1) // 2 
                stop = i + length // 2
        return s[start:stop+1]

    def expandFromCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left, right = left - 1, right + 1
        return right - left - 1 