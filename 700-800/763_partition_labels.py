class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = []
        start = end = 0
        lastIndexHashMap = {v : i for i, v in enumerate(S)}
        for i in range(len(S)):
            end = max(end, lastIndexHashMap[S[i]])
            if i == end:
                res.append(end - start + 1)
                start = 1 + end
        return res
