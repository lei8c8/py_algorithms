# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return None
        traversal_q, i, res = deque([root]), 1, []
        while traversal_q:
            level_len = len(traversal_q)
            level_nodes = []
            while level_len > 0:
                node = traversal_q.popleft()
                level_nodes.append(node.val)
                if node.left:
                    traversal_q.append(node.left)
                if node.right:
                    traversal_q.append(node.right)
                level_len -= 1
            if i % 2 == 0:
                res.append(level_nodes[::-1])
            else:
                res.append(level_nodes)
            i += 1
        return res