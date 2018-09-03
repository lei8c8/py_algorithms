import math

class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        W = int(math.sqrt(area))
        while area % W != 0:
            W -= 1
        return [area // W, W]

if __name__ == "__main__":
    solution = Solution()
    testdata = 9999991
    result = solution.constructRectangle(testdata)
    print(result)