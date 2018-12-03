class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        topView, rightView, res = [], [], 0
        for i in range(len(grid)):
            rightView.append(max(grid[i]))
        for i in range(len(grid[0])):
            maxVal = -1
            for j in range(len(grid)):
                maxVal = max(maxVal, grid[j][i])
            topView.append(maxVal)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += min(rightView[i], topView[j]) - grid[i][j]
        return res


if __name__ == "__main__":
    s = Solution()
    testdata = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
    r = s.maxIncreaseKeepingSkyline(testdata)
    print(r)
