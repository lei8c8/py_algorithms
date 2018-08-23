class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = []
        for s in str:
            res.append(s.lower())
        return ''.join(res)

if __name__ == '__main__':
    solution = Solution()
    result = solution.toLowerCase('HeLLo')
    print(result)