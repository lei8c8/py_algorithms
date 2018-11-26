from collections import deque

class Solution:
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        res = 0
        if len(nestedList) == 0:
            return res
        stack = deque()
        for ele in nestedList:
            stack.append((ele, 1))
        while stack:
            item, weight = stack.popleft()
            if item.isInteger():
                res += weight * item.getInteger()
            else:
                for i in item.getList():
                    stack.append((i, weight+1))
        return res

