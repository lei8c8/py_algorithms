# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return root
        else:
            if root.val < val:
                if root.right is None:
                    root.right = TreeNode(val)
                else:
                    self.insertIntoBST(root.right, val)
            if root.val > val:
                if root.left is None:
                    root.left = TreeNode(val)
                else:
                    self.insertIntoBST(root.left, val)
        return root      