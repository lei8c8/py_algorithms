from collections import deque

class Solution:
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None: return True
        q, f = deque([root]), False
        while q:
            n = q.popleft()
            if n.left:
                if f == True:
                    return False
                q.append(n.left)
            else:
                f = True
            if n.right:
                if f == True:
                    return False 
                q.append(n.right)
            else:
                f = True
        return True



        