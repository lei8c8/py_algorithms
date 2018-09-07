class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        row1 = [1]
        row2 = [1, 1]
        result = []
        if numRows == 0:
            return []
        elif numRows == 1:
            return [row1]
        elif numRows == 2:
            return [row1, row2]
        else:
            result.append(row1)
            result.append(row2)
            for i in range(2, numRows):
                row = [1]
                for j in range(1, i):
                    row.append(result[i-1][j-1] + result[i-1][j])
                row.append(1)
                result.append(row)
        return result