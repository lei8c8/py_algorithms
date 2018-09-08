class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        res = []
        self.dfs(t, res)
        res = [str(i) for i in res]
        return ''.join(res)

    def dfs(self, t, res):
        if not t:
            return None
        res.append(t.val)
        if t.left or t.right:
            res.append('(')
            self.dfs(t.left, res)
            res.append(')')
        if t.right:
            res.append('(')
            self.dfs(t.right, res)
            res.append(')')