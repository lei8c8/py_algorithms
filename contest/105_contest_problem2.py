class Solution:
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if max(A) < 0:
            return max(A)
        max_default = self.helper(A)
        wrap = 0
        for i in range(len(A)):
            wrap += A[i]
            A[i] = 0 - A[i]
        wrap += self.helper(A)
        if wrap > max_default:
            return wrap
        else:
            return max_default

    def helper(self, A):
        max_, max_e = 0, 0
        for i in range(len(A)):
            max_e += A[i]
            if max_e < 0: max_e = 0
            if max_ < max_e: max_ = max_e
        return max_

if __name__ == '__main__':
    solution = Solution()
    testdata1 = [1,-2,3,-2]
    testdata2 = [5,-3,5]
    testdata3 = [3,-1,2,-1]
    testdata4 = [3,-2,2,-3]
    testdata5 = [-2,-3,-1]
    result1 = solution.maxSubarraySumCircular(testdata1)
    result2 = solution.maxSubarraySumCircular(testdata2)
    result3 = solution.maxSubarraySumCircular(testdata3)
    result4 = solution.maxSubarraySumCircular(testdata4)
    result5 = solution.maxSubarraySumCircular(testdata5)
    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)
