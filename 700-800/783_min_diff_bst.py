# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math
class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodes = []
        self.inorderTraversal(root, nodes)
        res = math.inf
        for i in range(len(nodes) - 1):
            if nodes[i+1] - nodes[i] < res:
                res = nodes[i+1] - nodes[i]
        return res        

    def inorderTraversal(self, root, nodes):
        current = root
        if current is None:
            return
        self.inorderTraversal(current.left, nodes)
        nodes.append(current.val)
        self.inorderTraversal(current.right, nodes)
            