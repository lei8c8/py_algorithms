# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        traversal_queue = deque([root])
        ans = []
        while traversal_queue:
            level_len = len(traversal_queue)
            level_nodes = []
            while level_len > 0:
                node = traversal_queue.popleft()
                level_nodes.append(node.val)
                if node.left:
                    traversal_queue.append(node.left)
                if node.right:
                    traversal_queue.append(node.right)
                level_len -= 1
            ans.append(level_nodes)
        return ans