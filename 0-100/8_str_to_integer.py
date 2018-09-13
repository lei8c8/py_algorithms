class Solution:
    def myAtoi(self, str1):
        """
        :type str: str
        :rtype: int
        """
        try:
            temp = str1.split()[0]
        except:
            return 0
        if '.' in temp:
            temp = temp.split('.')[0]
        try:
            temp = int(temp)
        except:
            temp = 0
        if temp < 0 - 2 ** 31:
            temp = 0 - 2 ** 31
        if temp > 2 ** 31 - 1:
            temp = 2 ** 31 -1 
        return temp

if __name__ == "__main__":
    solution = Solution()
    testdata1 = "42"
    testdata2 = "   -42"
    testdata3 = "4193 with words"
    testdata4 = "words and 987"
    testdata5 = "-91283472332"
    testdata6 = ""
    testdata7 = "-3.14159"
    testresult1 = solution.myAtoi(testdata1)
    testresult2 = solution.myAtoi(testdata2)
    testresult3 = solution.myAtoi(testdata3)
    testresult4 = solution.myAtoi(testdata4)
    testresult5 = solution.myAtoi(testdata5)
    testresult6 = solution.myAtoi(testdata6)
    testresult7 = solution.myAtoi(testdata7)
    print(testresult1)
    print(testresult2)
    print(testresult3)
    print(testresult4)
    print(testresult5)
    print(testresult6)
    print(testresult7)