class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        for i in range(num + 1):
            res.append(bin(i)[2:].count('1'))
        return res