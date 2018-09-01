import math
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x         
        while left <= right:
            middle = (left + right) // 2
            if middle * middle == x:
                return middle
            elif middle * middle > x:
                right = middle -1
            else:
                left = middle + 1
        return left - 1

if __name__ == '__main__':
    solution = Solution()
    testdata = 8
    result = solution.mySqrt(testdata)
    print(result)