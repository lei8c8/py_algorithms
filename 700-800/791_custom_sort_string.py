class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        lookup = {}
        for i, v in enumerate(S):
            lookup[v] = i
        T2 = [(lookup[i], i) if i in lookup else (len(S), i) for i in T]
        T2.sort()
        T = [x[1] for x in T2]
        return ''.join(T)


if __name__ == "__main__":
    s = Solution()
    data1 = "cba"
    data2 = "abcd"
    r = s.customSortString(data1, data2)
    print(r)