class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        top = sideA = sideB = temp = 0
        for i in range(len(grid)):
            sideA += max(grid[i])
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    top += 1
        for k in range(len(grid[0])):
            for l in range(len(grid)):
                if grid[l][k] > temp:
                    temp = grid[l][k]
            sideB += temp
            temp = 0

        return top + sideA + sideB