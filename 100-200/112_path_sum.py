# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        lookup_parent = {root: None}
        traversal_queue = deque([root])
        leaves = []
        while len(traversal_queue) > 0:
            node = traversal_queue.popleft()
            if node.left:
                lookup_parent[node.left] = node
                traversal_queue.append(node.left)
            if node.right:
                lookup_parent[node.right] = node
                traversal_queue.append(node.right)
            if not node.left and not node.right:
                leaves.append(node)
        for n in leaves:
            sum_val = 0
            while n is not None:
                sum_val += n.val
                n = lookup_parent[n]
            if sum_val == sum:
                return True
        return False