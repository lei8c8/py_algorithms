
from collections import deque

class Solution:
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        qA, qB = deque([root1]), deque([root2])
        parentLookupA, parentLookupB = self.bfs(qA), self.bfs(qB)
        return parentLookupB == parentLookupA

    def bfs(self, q):
        parentLookup = {}
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
                parentLookup[node.left.val] = node.val
            if node.right:
                q.append(node.right)
                parentLookup[node.right.val] = node.val
        

