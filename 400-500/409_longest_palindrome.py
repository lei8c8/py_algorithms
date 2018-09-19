class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, lookup, single = 0, {}, 0
        for ch in s:
            if ch not in lookup:
                lookup[ch] = 1
            else:
                lookup[ch] += 1
        for key in lookup:
            if lookup[key] % 2 == 0:
                res += lookup[key]
            elif lookup[key] % 2 == 1:
                res += (lookup[key] - 1)
                single = 1

        return res + single