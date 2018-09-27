class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lookup_s, lookup_t = {}, {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in lookup_s:
                lookup_s[s[i]] = t[i]
            if t[i] not in lookup_t:
                lookup_t[t[i]] = s[i]
            if lookup_s[s[i]] != t[i] or lookup_t[t[i]] != s[i]:
                return False
        return True