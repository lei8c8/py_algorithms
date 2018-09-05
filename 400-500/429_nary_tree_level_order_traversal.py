"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        queue = deque([root])
        while len(queue) > 0:
            level_len = len(queue)
            temp = []
            while level_len > 0:
                node = queue.popleft()
                temp.append(node.val)
                while node.children:
                    queue.append(node.children.pop(0))
                level_len -= 1
            res.append(temp)
        return res