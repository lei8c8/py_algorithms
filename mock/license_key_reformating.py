class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.split('-')
        S = ''.join(S)
        S = S.upper()
        res = []
        mod = len(S) % K
        if mod == 0:
            i = 0
            while i < len(S):
                res.append(S[i:K+i])
                i += K
            return '-'.join(res)
        else:
            res.append(S[0:mod])
            i = mod
            while i < len(S):
                res.append(S[i:K+i])
                i += K
            return '-'.join(res)

if __name__ == "__main__":
    solution = Solution()
    testdata = "5F3Z-2e-9-w"
    result = solution.licenseKeyFormatting(testdata, 3)
    print(result)

