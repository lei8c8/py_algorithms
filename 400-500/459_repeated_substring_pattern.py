class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 1
        while i <= len(s) // 2:
            j = i
            while j <= len(s) - i:
                if s[0:i] != s[j:j+i]:
                    break
                if j + i == len(s):
                    return True
                j += i
            i += 1
        return False