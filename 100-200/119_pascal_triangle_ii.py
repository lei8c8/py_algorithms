class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row1 = [1]
        row2 = [1, 1]
        result = []
        if rowIndex == 0:
            return row1
        elif rowIndex == 1:
            return row2
        else:
            result.append(row1)
            result.append(row2)
            for i in range(2, rowIndex + 1):
                row = [1]
                for j in range(1, i):
                    row.append(result[i-1][j-1] + result[i-1][j])
                row.append(1)
                result.append(row)
        return result[-1]