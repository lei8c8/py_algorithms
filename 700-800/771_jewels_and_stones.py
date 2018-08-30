class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = set(list(J))
        res = 0
        for c in S:
            if c in jewels:
                res += 1
        return res

if __name__ == '__main__':
    solution = Solution()
    result = solution.numJewelsInStones("aA", "aAAbbbb")
    print(result)