class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        a = b = 0
        d1, d2 = {}, {}
        for s, e in zip(secret, guess):
            if s == e:
                a += 1
            else:
                if s not in d1:
                    d1[s] = 1
                else:
                    d1[s] += 1
                if e not in d2:
                    d2[e] = 1
                else:
                    d2[e] += 1
        for key in d1:
            b += min(d1[key], d2.get(key, 0))
        return str(a) + 'A' + str(b) + 'B'


if __name__ == "__main__":
    solution = Solution()
    testdata1 = "1123"
    testdata2 = "0111"
    result = solution.getHint(testdata1, testdata2)
    print(result)