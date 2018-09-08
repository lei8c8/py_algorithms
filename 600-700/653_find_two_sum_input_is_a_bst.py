class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root is None: return False
        lookup = set()
        bfs_queue = [root]
        for node in bfs_queue:
            if k - node.val in lookup: return True
            lookup.add(node.val)
            if node.left: bfs_queue.append(node.left)
            if node.right: bfs_queue.append(node.right)
        return False