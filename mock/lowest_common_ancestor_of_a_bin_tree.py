from collections import deque
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        parent_lookup = {}
        if not root:
            return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                parent_lookup[node.left] = node
                queue.append(node.left)
            if node.right:
                parent_lookup[node.right] = node
                queue.append(node.right)
        p_p = set()
        while True:
            p_p.add(p)
            try:
                p = parent_lookup[p]
            except:
                break

        while q:
            if q in p_p:
                return q
            q = parent_lookup[q]