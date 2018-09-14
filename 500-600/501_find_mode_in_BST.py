from collections import Counter
from collections import deque

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = deque([root])
        my_list = []
        res = []
        while queue:
            node = queue.popleft()
            my_list.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ct = Counter(my_list)
        occ = ct.most_common(1)[0][1]
        for key in ct:
            if ct[key] == occ:
                res.append(key)
        return res