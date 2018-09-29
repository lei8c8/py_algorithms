class Solution(object):
    def isValidSudoku(self, board):
      
        rowsum=[{} for i in range(9)]
        colsum=[{} for j in range(9)]
        local=[[{} for i in range(3)] for j in range(3)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]!='.':
                    ele=board[i][j]
                    rowsum[i][ele]=rowsum[i].get(ele,0)+1
                    colsum[j][ele]=colsum[j].get(ele,0)+1
                    local[i//3][j//3][ele]=local[i//3][j//3].get(ele,0)+1
        flag=True
        for e in rowsum:
            if len(e.values())>0 and max(e.values())>1:
                return False
        for e in colsum:
            if len(e.values())>0 and max(e.values())>1:
                return False
        for row in local:
            for dic in row:
                if len(dic.values())>0 and max(dic.values())>1:
                    return False
        return True