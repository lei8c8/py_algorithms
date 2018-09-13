# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        lookup_parent = {root: None}
        traversal_queue = deque([root])
        leaves = []
        target = []
        total = 0
        while traversal_queue:
            node = traversal_queue.popleft()
            if node.left:
                lookup_parent[node.left] = node
                traversal_queue.append(node.left)
            if node.right:
                lookup_parent[node.right] = node
                traversal_queue.append(node.right)
            if not node.left and not node.right:
                leaves.append(node)
        for leaf in leaves:
            temp = [leaf.val]
            while lookup_parent[leaf] != None:
                temp.append((lookup_parent[leaf]).val)
                leaf = lookup_parent[leaf]
            target.append(temp)
        for arr in target:
            arr = int(''.join([str(i) for i in arr])[::-1])
            total += arr
        return total