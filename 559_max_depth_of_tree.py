"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution():
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        def traverse(root):
            if root is None:
                return 0
            depth = 0
            queue = deque([root])
            while len(queue) > 0:
                level_length = len(queue)
                while level_length > 0:
                    node = queue.popleft()
                    for n in node.children:
                        queue.append(n)
                    level_length -= 1
                depth += 1
            return depth

        return traverse(root)