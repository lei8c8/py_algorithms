class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1]
        sum = 0
        for i in range(len(s)):
            if i == 0:
                v = ord(s[i]) - ord('A') + 1
            else:
                v = (ord(s[i]) - ord('A') + 1) * 26 * i
            sum += v
        return sum


if __name__ == '__main__':
    solution = Solution()
    testdata = 'AB'
    print(solution.titleToNumber(testdata))