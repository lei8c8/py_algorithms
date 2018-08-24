class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for word in s.split(' '):
            res.append(word[::-1])
        return ' '.join(res)

if __name__ == '__main__':
    solution = Solution()
    testdata = "Let's take LeetCode contest"
    result = solution.reverseWords(testdata)
    print(result)