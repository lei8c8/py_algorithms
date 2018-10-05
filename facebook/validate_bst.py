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
        if len(set(res)) != len(res):
            return False
        return res == sorted(res)
        
    def inorder(self, node, list):
        if node.left: 
            self.inorder(node.left, list)
        list.append(node.val)
        if node.right:
            self.inorder(node.right, list)