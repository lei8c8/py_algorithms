# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        if not root: return 0
        queue = deque([root])
        while queue:
            level_len = len(queue)
            while level_len > 0:
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                if not node.right and not node.left:
                    return res
                level_len -= 1
            res += 1
