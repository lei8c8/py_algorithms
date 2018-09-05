class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        island_by_4 = 0
        internal_edge = 0
        if not grid:
            return False

        if len(grid) == 1:
            for i in range(len(grid[0])):
                if grid[0][i] == 1:
                    island_by_4 += 4
                    if i <= len(grid[0]) - 2:
                        if grid[0][i+1] == 1:
                            internal_edge += 1
            return island_by_4 - 2 * internal_edge

        if len(grid[0]) == 1:
            for i in range(len(grid)):
                if grid[i][0] == 1:
                    island_by_4 += 4
                    if i <= len(grid) - 2:
                        if grid[i+1][0] == 1:
                            internal_edge += 1
            return island_by_4 - 2 * internal_edge

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    island_by_4 += 4
                    if i <= (len(grid) - 2) and j <= (len(grid[0]) - 2):
                        if grid[i][j+1] == 1:
                                internal_edge += 1
                        if grid[i+1][j] == 1:
                                internal_edge += 1
                    if i == len(grid) - 1 and j != len(grid[0]) - 1 :
                        if grid[i][j+1] == 1:
                            internal_edge += 1
                    if j == len(grid[0]) - 1 and i != len(grid) - 1:
                        if grid[i+1][j] == 1:
                            internal_edge += 1
        return island_by_4 - 2 * internal_edge