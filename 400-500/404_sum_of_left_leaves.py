# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = 0

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        if root is None:
            return None
        if root.left and root.left.left is None and root.left.right is None:
            self.res += root.left.val
        self.dfs(root.left)
        self.dfs(root.right)
