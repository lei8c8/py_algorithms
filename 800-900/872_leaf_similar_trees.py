# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        list1 = []
        list2 = []
        def traverse(root, myList):
            if root is None:
                return None
            elif root.left is None and root.right is None:
                myList.append(root.val)
            else:
                traverse(root.left, myList)
                traverse(root.right, myList)

        traverse(root1, list1)
        traverse(root2, list2)
        return list1 == list2