class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        current = root
        while current:
            if current.val == val:
                return current
            elif current.val > val:
                current = current.left
            else:
                current = current.right
        return None