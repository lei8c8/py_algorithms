class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        res, res_right = [], []
        self.postorder(root, res)
        self.postorder2(root, res_right)
        return res == res_right

    def postorder(self, node, res):
        cur = node
        if cur.left:
            self.postorder(cur.left, res)
        else:
            res.append(None)
        if cur.right:
            self.postorder(cur.right, res)
        else:
            res.append(None)
        res.append(cur.val)

    def postorder2(self, node, res):
        cur = node
        if cur.right:
            self.postorder2(cur.right, res)
        else:
            res.append(None)
        if cur.left:
            self.postorder2(cur.left, res)
        else:
            res.append(None)
        res.append(cur.val)