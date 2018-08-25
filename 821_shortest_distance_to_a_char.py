class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        indexSet = set()
        res = []
        for i in range(len(S)):
            if S[i] == C:
                indexSet.add(i)
        for i in range(len(S)):
            shortest = 1001
            for j in indexSet:
                if abs(i - j) < shortest:
                    shortest = abs(i -j)
            res.append(shortest)
        return res


