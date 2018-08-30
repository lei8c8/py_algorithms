# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return None
        traversal_queue = deque([root])
        res = []
        while len(traversal_queue) > 0:
            level_number = len(traversal_queue)
            level_count = len(traversal_queue)
            level_sum = 0
            while level_number > 0:
                node = traversal_queue.popleft()
                if node.left:
                    traversal_queue.append(node.left)
                if node.right:
                    traversal_queue.append(node.right)
                level_number -= 1
                level_sum += node.val
            avg = level_sum / level_count
            res.append(avg)
        return res
