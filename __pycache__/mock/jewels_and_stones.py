class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        lookup = set(list(J))
        res = 0 
        for ele in S:
            if ele in lookup:
                res += 1
        return res