class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        lookup1, lookup2 = {}, {}
        n, m = len(pattern), len(str.split())
        if n != m: return False
        str = str.split()
        for i in range(n):
            if pattern[i] not in lookup1:
                lookup1[pattern[i]] = str[i]
            if str[i] not in lookup2:
                lookup2[str[i]] = pattern[i]
            if lookup1[pattern[i]] != str[i] or lookup2[str[i]] != pattern[i]:
                return False
        return True