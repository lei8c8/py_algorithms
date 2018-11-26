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
        leaves = []
        parentLookup = {}
        q = deque([root])
        res = 0
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
                parentLookup[node.left] = node
            if node.right:
                q.append(node.right)
                parentLookup[node.right] = node
            if not node.left and not node.right:
                leaves.append(node)
        for leave in leaves:
            tmp = []
            l = leave
            while l is not root:
                tmp.append(str(l.val))
                l = parentLookup[l]
            tmp.append(str(root.val))
            value = int(''.join(tmp[::-1]))
            res += value
        return res