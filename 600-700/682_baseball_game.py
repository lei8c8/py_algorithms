class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        valid = []
        for i in ops:
            if i not in ('C', 'D', '+'):
                valid.append(int(i))
            elif i == 'C':
                valid.pop()
            elif i == 'D':
                valid.append(valid[-1] * 2)
            else:
                valid.append(valid[-1] + valid[-2])

        return sum(valid)

if __name__ == '__main__':
    solution = Solution()
    testdata = ["5","2","C","D","+"]
    testcase = solution.calPoints(testdata)
    print(testcase)