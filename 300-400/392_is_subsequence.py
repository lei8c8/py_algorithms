class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s: return True
        j = 0
        for i in range(len(t)):
            if t[i] == s[j]:
                j += 1
        return j == len(s)