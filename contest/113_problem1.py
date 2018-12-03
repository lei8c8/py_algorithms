import itertools

class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        p = list(itertools.permutations(A))
        p2, res = [], []
        for e in p:
            p2.append((e[0] * 10 + e[1], e[2] * 10 + e[3]))
        p2.sort(key = lambda x: -x[0])
        for hh, mm in p2:
            if 0 <= hh <= 23 and 0 <= mm <=59:
                res.append((hh, mm))
        if len(res) == 0: return ""
        res.sort(key = lambda x: (-x[0], -x[-1]))
        hh, mm = str(res[0][0]), str(res[0][-1])
        if len(hh) == 1: hh = '0' + hh
        if len(mm) == 1: mm = '0' + mm
        return hh + ':' + mm
        



if __name__ == "__main__":
    s = Solution()
    data = [1,5,6,3]
    result = s.largestTimeFromDigits(data)
    print(result)