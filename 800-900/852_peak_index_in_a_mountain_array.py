class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(1,len(A)):
            if A[i] < A[i-1]:
                return i - 1

if __name__ == '__main__':
    solution = Solution()
    testdata = [0,2,1,0]
    result = solution.peakIndexInMountainArray(testdata)
    print(result)