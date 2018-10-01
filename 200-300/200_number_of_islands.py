from collections import deque

class Solution:
    def __init__(self):
        self.count = 0

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    self.count += 1
        return self.count

    def dfs(self, grid, i, j):
        four_dirs = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        dfs_queue = deque()
        for x, y in four_dirs:
            dfs_queue.append((x, y))
        while dfs_queue:
            d1, d2 = dfs_queue.popleft()
            if 0 <= d1 < len(grid) and 0 <= d2 < len(grid[0]) and grid[d1][d2] == '1':
                grid[d1][d2] = '0' 
                four_dirs = [(d1+1, d2), (d1-1, d2), (d1, d2+1), (d1, d2-1)]
                for x, y in four_dirs:
                    dfs_queue.append((x,y))

if __name__ == "__main__":
    sol = Solution()
    testdata = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    result = sol.numIslands(testdata)
    print(result)