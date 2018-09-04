class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        res = []
        new_S = self.remove_dash(S)
        first_length = len(new_S) % K
        if first_length == 0:
            first_length = K
        res.append(new_S[:first_length])
        for i in range(first_length, len(new_S), K):
            res.append(new_S[i:i+K])
        return '-'.join(res)

    def remove_dash(self, S):
        res = []
        for ch in S:
            if ch is not "-":
                res.append(ch.upper())
        return ''.join(res)