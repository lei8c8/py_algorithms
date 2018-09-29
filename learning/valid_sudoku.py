class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        i, j = 0, 0
        while i < 7:
            while j < 7:       
                temp = []
                row1 = [board[i][j], board[i][j+1], board[i][j+2]]
                row2 = [board[i+1][j], board[i+1][j+1], board[i+1][j+2]]
                row3 = [board[i+2][j], board[i+2][j+1], board[i+2][j+2]]
                temp = [row1, row2, row3]
                if not self.isValidSudokuBlock(temp):
                    return False
                j += 3
            i += 3
        if not self.isValidSudokuRowOrColumn(board):
            return False
        return True

    def isValidSudokuBlock(self, arr):
        nums = []
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] != '.':
                    nums.append(arr[i][j])
        return len(nums) == len(set(nums))
    
    def isValidSudokuRowOrColumn(self, arr):
        temp1 = []
        temp2 = []
        for i in range(len(arr)):
            rows = []
            for j in range(len(arr[0])):
                if arr[i][j] != '.':
                    rows.append(arr[i][j])
            temp1.append(rows)
        for j in range(len(arr[0])):
            columns = []
            for i in range(len(arr)):
                if arr[i][j] != '.':
                    columns.append(arr[i][j])
            temp2.append(columns)
        print(temp2)
        for line in temp1:
            if len(line) != len(set(line)):
                return False
        for line in temp2:
            if len(line) != len(set(line)):
                return False
        return True
            


if __name__ == '__main__':
    solution = Solution()
    testdata = [
        [".",".","4",".",".",".","6","3","."],
        [".",".",".",".",".",".",".",".","."],
        ["5",".",".",".",".",".",".","9","."],
        [".",".",".","5","6",".",".",".","."],
        ["4",".","3",".",".",".",".",".","1"],
        [".",".",".","7",".",".",".",".","."],
        [".",".",".","5",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."]]
    result = solution.isValidSudoku(testdata)
    print(result)