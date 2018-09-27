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

solution = Solution()
testdata = [[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]
result = solution.findLongestChain(testdata)
print(result)