class Solution:
    def checkRecord(self, s):
        return False if 'LLL' in s or s.count('A') > 1 else True
