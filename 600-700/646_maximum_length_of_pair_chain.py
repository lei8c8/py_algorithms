class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if not pairs:
            return 0
        if len(pairs) == 1:
            return 1
        pairs.sort(key = lambda x: x[1])
        temp = []
        temp.append(pairs[0])
        for i in range(1, len(pairs)):
            if pairs[i][0] > temp[-1][-1]:
                temp.append(pairs[i])
        return len(temp)