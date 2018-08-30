# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(root):
            if not root:
                return 0
            depth = 0
            traversal_queue = deque([root])
            while len(traversal_queue) > 0:
                level_len = len(traversal_queue)
                while level_len > 0:
                    node = traversal_queue.popleft()
                    if node.left:
                        traversal_queue.append(node.left)
                    if node.right:
                        traversal_queue.append(node.right)
                    level_len -= 1
                depth += 1
            return depth
        return traverse(root)