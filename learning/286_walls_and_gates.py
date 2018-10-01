from collections import deque

class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    self.dfs(rooms, i, j)
    

    def dfs(self, rooms, i, j):
        four_dirs = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        dfs_queue = deque()
        for x, y in four_dirs:
            dfs_queue.append((x, y, 1))
        while dfs_queue:
            d1, d2, n = dfs_queue.popleft()
            if 0 <= d1 < len(rooms) and 0 <= d2 < len(rooms[0]) and rooms[d1][d2] > n:
                rooms[d1][d2] = n
                four_dirs = [(d1+1, d2), (d1-1, d2), (d1, d2+1), (d1, d2-1)]
                for x, y in four_dirs:
                    dfs_queue.append((x, y, n+1))