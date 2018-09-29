class Solution(object):
    def findDuplicateSubtrees(self, root):
        self.res = []
        self.dic = {}
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        if not root: return '#'
        tree = self.dfs(root.left) + self.dfs(root.right) + str(root.val)
        if tree in self.dic and self.dic[tree] == 1:
            self.res.append(root)
        self.dic[tree] = self.dic.get(tree, 0) + 1
        return tree