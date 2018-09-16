# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []
        self.inorder(root, res)
        return res[k-1]

    def inorder(self, root, res):
        cur, count= root, 0
        if not cur: return None
        self.inorder(cur.left, res)
        res.append(cur.val)
        self.inorder(cur.right, res)
