"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        self.helper(root, res)
        return res
    

    def helper(self, root, res):
        current = root
        res.append(current.val)
        while current.children:
            node = current.children.pop(0)
            self.helper(node, res)