class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''base case'''
        if n == 1:
            return 1
        elif n== 2:
            return 2
        temp = [1, 2]
        for i in range(2, n):
            temp.append(temp[i-1] + temp[i-2])
        return temp[-1]

if __name__ == '__main__':
    solution = Solution()
    testdata = 3
    result = solution.climbStairs(testdata)
    print(result)