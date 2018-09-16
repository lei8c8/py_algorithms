# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def findBottomLeftValue(self, root):
        traversal_q, res = deque([root]), 0
        while traversal_q:
            level_len, first_lev_node = len(traversal_q), True
            while level_len > 0:
                node = traversal_q.popleft()
                if first_lev_node:
                    res = node.val
                if node.left:
                    traversal_q.append(node.left)
                if node.right:
                    traversal_q.append(node.right)
                level_len -= 1
                first_lev_node = False
        return res       