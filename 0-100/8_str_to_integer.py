class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        temp = str.strip()
        if not temp:
            return 0
        negative = False
        resint = 0
        head = temp[0]
        if head == "-":
            negative = True
        elif head == "+":
            negative = False
        elif not head.isnumeric():
            return 0
        else:
            resint += ord(head) - ord('0')
        for i in range(1,len(temp)):
            if temp[i].isnumeric():
                resint = 10*resint + ord(temp[i]) - ord('0')
                if not negative and resint >= 2147483647:
                    return 2147483647
                if negative and resint >= 2147483648:
                    return -2147483648
            else:
                break
        if not negative:
            return resint
        else:
            return -resint

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