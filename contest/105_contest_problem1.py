class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        if S == '':
            return ''
        temp = list(S)
        temp2 = []
        for e in temp:
            if e.isalpha():
                temp2.append(e)
        for i in range(len(temp)):
            if temp[i].isalpha():
                v = temp2.pop()
                temp[i] = v
        return ''.join(temp)

if __name__ == '__main__':
    solution = Solution()
    testdata = "Test1ng-Leet=code-Q!"
    result = solution.reverseOnlyLetters(testdata)
    print(result)