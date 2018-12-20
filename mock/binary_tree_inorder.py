class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.dfs(root, res)
        return res
        
    def dfs(self, node, list):
        if not node: return node 
        if node.left:
            self.dfs(node.left, list)
        list.append(node.val)
        if node.right:
            self.dfs(node.right, list)
