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
        if not root: return 0
        if not root.right and not root.left: return 1
        res = 0
        traversal_queue = deque([root])
        while traversal_queue:
            level_len = len(traversal_queue)
            res += 1
            while level_len > 0:
                node = traversal_queue.popleft()
                if not node.left and not node.right:
                    return res
                if node.left:
                    traversal_queue.append(node.left)
                if node.right:
                    traversal_queue.append(node.right)
                level_len -= 1
