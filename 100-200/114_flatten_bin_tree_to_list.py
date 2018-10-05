class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        res = []
        if not root: return root
        self.preorder(root, res)
        cur = head = res[0]
        for i in range(1, len(res)):
            cur.left = None
            cur.right = res[i]
            cur = res[i]

    def preorder(self, root, res):
        cur = root
        res.append(cur)
        if cur.left: self.preorder(cur.left, res)
        if cur.right: self.preorder(cur.right, res)