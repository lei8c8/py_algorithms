class Solution:
    def diameterOfBinaryTree(self, root):
        self.length = 1
        def dfs(node):
            if not node:
                return 0
            left_length = dfs(node.left)
            right_length = dfs(node.right)
            self.length = max(self.length, left_length + right_length + 1)
            return max(left_length, right_length) + 1
        dfs(root)
        return self.length - 1

        