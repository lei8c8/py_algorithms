# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        res = []
        self.inorder(root, res)
        return res == sorted(res) and len(res) == len(set(res))

    def inorder(self, root, res):
        cur = root
        if cur.left:
            self.inorder(cur.left, res)
        res.append(cur.val)
        if cur.right:
            self.inorder(cur.right, res)