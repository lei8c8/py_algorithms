from math import sqrt

class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i = 0
        while i**2 <= c:
            b = sqrt(c - i ** 2)
            if b == int(b): return True
            i += 1
        return False