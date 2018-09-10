class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        length = len(S)
        if length < 3:
            return []
        S = S + '@'
        res = []
        pointer = S[0]
        count = 0
        for i in range(length + 1):
            if S[i] == pointer:
                count += 1
            else:
                if count >= 3:
                    res.append([i - count, i - 1])
                    count = 1
                    pointer = S[i]
        return res