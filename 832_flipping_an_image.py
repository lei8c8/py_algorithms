class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            A[i].reverse()
        for j in range(len(A)):
            for k in range(len(A[0])):
                if A[j][k] == 1:
                    A[j][k] = 0
                else:
                    A[j][k] = 1
        return A

if __name__ == '__main__':
    solution = Solution()
    test = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    testcase = solution.flipAndInvertImage(test)
    print(test)