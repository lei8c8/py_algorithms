class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_list = self.path(p, root)
        q_list = self.path(q, root)
        min_len = min(len(p_list), len(q_list))
        for i in range(min_len):
            if p_list[i] != q_list[i]:
                return p_list[i - 1]
        return p_list[min_len - 1]
        
    def path(self, search, node):
        res = []
        current = node
        if not current:
            return res
        while True:
            if current.val == search.val:
                res.append(current)
                return res
            elif current.val > search.val:
                res.append(current)
                current = current.left
            else:
                res.append(current)
                current = current.right

