class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        else:
            s = s.split()
            if len(s) == 0:
                return 0
            else:
                return len(s[-1])