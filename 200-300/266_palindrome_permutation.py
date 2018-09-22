from collections import Counter
class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_len = len(s)
        ct = Counter(s)
        single = 0
        if s_len % 2 == 0:
            for key in ct:
                if ct[key] % 2 != 0:
                    return False
            return True
        else:
            for key in ct:
                if ct[key] % 2 != 0:
                    single += 1
            if single != 1:
                return False
            else:
                return True
        