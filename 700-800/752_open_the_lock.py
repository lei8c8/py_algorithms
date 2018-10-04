from collections import deque

class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        visited = set(['0000'])
        dead = set(deadends)
        queue = deque([('0000',0)])
        while queue:
            node, depth = queue.popleft()
            if node in dead:
                continue
            if node == target:
                return depth
            for n in self.find_neighbors(node):
                if n not in visited:
                    visited.add(n)
                    queue.append((n, depth + 1))
        return -1
        
    def find_neighbors(self, node):
        for i in range(4):
            x = int(node[i])
            for plus_mins in (1, -1):
                y = (x + plus_mins) % 10
                yield node[:i] + str(y) + node[i+1:]
