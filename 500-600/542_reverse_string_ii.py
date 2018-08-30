class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        temp = []
        i = 0
        c = 0
        while i < len(s):
            if c % 2 == 0:
                temp.append(s[i:i+k][::-1])
            else:
                temp.append(s[i:i+k])
            i += k
            c += 1
        return ''.join(temp)

if __name__ == "__main__":
    solution = Solution()
    testdata = 'abcdefg'
    result = solution.reverseStr(testdata, 3)
    print(result)
