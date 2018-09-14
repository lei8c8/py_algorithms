# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        self.dfs(root, res)
        return res

    def dfs(self, root, res):
        cur = root
        if cur.left:
            self.dfs(root.left, res)
        if cur.right:
            self.dfs(root.right, res)
        res.append(cur.val)