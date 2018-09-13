# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        res = []
        self.inorder(root, res)
        print(res)
        head = TreeNode(1)
        prev = head
        for element in res:
            node = TreeNode(element)
            prev.right = node
            prev = node
        return head.right


    def inorder(self, root, res):
        current = root
        if not current:
            return None
        self.inorder(current.left, res)
        res.append(current.val)
        self.inorder(current.right, res)