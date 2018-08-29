class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return 0
        count_list = []
        first = s[0]
        counter = 1
        res = 0
        for i in range(1, len(s)):
            if s[i] == first:
                counter += 1
            else:
                first = s[i]
                count_list.append(counter)
                counter = 1
        count_list.append(counter)
        for i in range(len(count_list) -1):
            res += min(count_list[i], count_list[i+1])
        return res

if __name__ == '__main__':
    solution = Solution()
    testdata = "0011100111111100001111001010111000"
    result = solution.countBinarySubstrings(testdata)
    print(result)