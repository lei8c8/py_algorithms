class Solution:
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        if N == 0: 
            return cells
        count = 0 
        cells_o = cells[:]
        res = []
        while count < 14:
            for i in range(len(cells)):
                if i == 0 or i == len(cells) - 1 :
                    cells[i] = 0
                else:
                    if (cells_o[i-1]  == 0 and cells_o[i+1] == 0) or (cells_o[i-1]  == 1 and cells_o[i+1] == 1):
                        cells[i] = 1
                    else:
                        cells[i] = 0
            cells_o = cells[:]          
            count += 1
            res.append(cells_o[:])
        print(res)
        if N % 14 == 0: return res[13]
        if N % 14 != 0:
            N = N % 14
        return res[(N-1)]
                

if __name__ == "__main__":
    s = Solution()
    result = s.prisonAfterNDays([0,1,0,1,1,0,0,1],7)
    print(str(result))