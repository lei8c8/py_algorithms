class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        from collections import Counter
        ct = Counter(A.split(" ")) + Counter(B.split(" "))
        res = []
        for k in ct:
            if ct[k] == 1:
                res.append(k)
        return res


if __name__ == '__main__':
    solution = Solution()
    result = solution.uncommonFromSentences("this apple is sweet", "this apple is sour")
    result2 = solution.uncommonFromSentences("app app", 'baa')
    print(result)
    print(result2)