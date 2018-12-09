class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = {}
        for element in s:
            if element not in lookup:
                lookup[element] = 1
            else:
                lookup[element] += 1
        for i in range(len(s)):
            if lookup[s[i]] == 1:
                return i
        return -1