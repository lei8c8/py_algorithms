from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        traversal_q = deque([root])
        res = []
        while traversal_q:
            level_len = len(traversal_q)
            while level_len > 0:
                node = traversal_q.popleft()
                if node.left:
                    traversal_q.append(node.left)
                if node.right:
                    traversal_q.append(node.right)
                level_len -= 1
                if level_len == 0:
                    res.append(node.val)
        return res