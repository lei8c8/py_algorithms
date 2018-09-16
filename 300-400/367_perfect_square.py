class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return True
        low, high = 1, num
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                high = mid - 1
            else:
                low = mid + 1
        return False

if __name__ == "__main__":
    solution = Solution()
    testdata1 = 16
    testdata2 = 14
    print(solution.isPerfectSquare(testdata1)) 
    print(solution.isPerfectSquare(testdata2)) 