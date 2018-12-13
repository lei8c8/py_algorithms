class Solution:
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        self.index, self.diff, res = 0, float('inf'), []
        self.inorder(root, target, res)
        self.index -= 1
        ans = [res[self.index]]
        left, right = self.index - 1, self.index + 1
        while k > 1:
            if left < 0 and right < len(res):
                ans.append(res[right])
                right += 1
            if right >= len(res) and left >= 0:
                ans.append(res[left])
                left -= 1
            if left >= 0 and right < len(res):
                if abs(target - res[left]) < abs(res[right] - target):
                    ans.append(res[left])
                    left -= 1
                else:
                    ans.append(res[right])
                    right += 1
            k -= 1
        return ans

        
    def inorder(self, root, target, res):
        cur = root
        if cur.left: self.inorder(cur.left, target, res)
        if abs(cur.val - target) < self.diff:
            self.diff = abs(cur.val - target)
            self.index += 1
        res.append(cur.val)
        if cur.right: self.inorder(cur.right, target, res)