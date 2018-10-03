from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix: return res
        group = defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                group[i+j].append(matrix[i][j])
        for key in sorted(group.keys()):
            if key % 2 == 0:
                group[key].reverse()
            res.extend(group[key])
        return res