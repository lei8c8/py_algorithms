class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if 'LLL' in s:
            return False
        if s.count('A') > 1:
            return False
        return True