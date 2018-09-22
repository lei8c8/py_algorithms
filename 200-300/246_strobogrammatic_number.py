class Solution:
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        lookup = {'2', '3', '4', '5', '7'}
        res = []
        for e in num:
            if e in lookup:
                return False
            else:
                res.append(self.upside_view(e))
        res.reverse()
        return ''.join(res) == num

    
    def upside_view(self, s):
        if s == '8' or s == '1' or s == '0':
            return s
        if s == '6':
            return '9'
        if s == '9':
            return '6'

if __name__ == "__main__":
    solution = Solution()
    testdata = "88"
    result = solution.isStrobogrammatic(testdata)
    print(result)