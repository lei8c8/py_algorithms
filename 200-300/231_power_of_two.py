class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n_bin = bin(n)[2:]
        if n_bin[0] == '1' and (n_bin.count('0') == len(n_bin) - 1):
            return True
        return False
