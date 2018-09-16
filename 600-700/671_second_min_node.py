# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return None
        traversal_queue = deque([root])
        node_vals = []
        while traversal_queue:
            node = traversal_queue.popleft()
            node_vals.append(node.val)
            if node.left: traversal_queue.append(node.left)
            if node.right: traversal_queue.append(node.right)
        list_after_del_dups = sorted(list(set(node_vals)))
        return -1 if len(list_after_del_dups) < 2 else list_after_del_dups[1]