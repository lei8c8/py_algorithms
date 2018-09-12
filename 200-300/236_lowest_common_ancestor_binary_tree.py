# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        lookup_parent = {root: None}
        traversal_queue = deque([root])
        visited_p = False
        visited_q = False
        p_parents = set()
        while len(traversal_queue) > 0:
            node = traversal_queue.popleft()
            if node == p:
                visited_p = True
            if node == q:
                visited_q = True
            if node.left:
                lookup_parent[node.left] = node
                traversal_queue.append(node.left)
            if node.right:
                lookup_parent[node.right] = node
                traversal_queue.append(node.right)
            if visited_p and visited_q:
                break
        while p is not None:
            p_parents.add(p)
            p = lookup_parent[p]          
        while q is not None:
            if q in p_parents:
                return q
            q = lookup_parent[q]
