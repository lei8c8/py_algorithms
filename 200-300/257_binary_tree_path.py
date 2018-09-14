# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root: return []
        if not root.left and not root.right: return [str(root.val)]
        res = []
        traversal_q = deque([root])
        lookup_parent = {root: None}
        node_leaves = []
        while len(traversal_q) > 0 :
            node = traversal_q.popleft()
            if node.left:
                lookup_parent[node.left] = node
                traversal_q.append(node.left)
            if node.right:
                lookup_parent[node.right] = node
                traversal_q.append(node.right)
            if not node.left and not node.right:
                node_leaves.append(node)
        for leaf in node_leaves:
            temp_list = []
            while leaf is not None:
                value = leaf.val
                temp_list.append(value)
                leaf = lookup_parent[leaf]
            res.append(temp_list)
        res = [x[::-1] for x in res]  
        for i in range(len(res)):
            for j in range(len(res[i])):
                res[i][j] = str(res[i][j])
            res[i] = "->".join(res[i])
        return res