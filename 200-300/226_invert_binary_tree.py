# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if not root.left and not root.right:
            return root
        if root.left or root.right:
            temp = root.left 
            root.left = root.right
            root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
