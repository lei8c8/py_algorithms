class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(A)
        columns = len(A[0])
        res = []
        for i in range(columns):
            new_columns = []
            for j in range(rows):
                new_columns.append(A[j][i])
            res.append(new_columns)
        return res

if __name__ == '__main__':
    solution = Solution()
    testdata = [[1,2,3],[4,5,6]]
    result = solution.transpose(testdata)
    print(result)