class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lookup1, lookup2 = {}, {}
        for i in range(len(s)):
            if s[i] not in lookup1:
                lookup1[s[i]] = t[i]
            if t[i] not in lookup2:
                lookup2[t[i]] = s[i]
            if lookup1[s[i]] != t[i] or lookup2[t[i]] != s[i]:
                return False
        return True