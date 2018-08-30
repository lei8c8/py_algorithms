class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for i in range(left, right + 1):
            itIs = True
            myList = set(str(i))
            if '0' in myList:
                continue
            for n in myList:
                if i % int(n) != 0:
                    itIs = False
                    break
            if itIs == True:
                res.append(i)
        return res            


if __name__ == '__main__':
    solution = Solution()
    test = solution.selfDividingNumbers(1,22)
    print(test)
