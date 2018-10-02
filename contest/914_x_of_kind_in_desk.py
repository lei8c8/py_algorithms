class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        d = {}
        res = []
        for v in deck:
            if v not in d:
                d[v] = 1
            else:
                d[v] += 1
        for key in d:
            res.append(d[key])
        res.sort()
        print(res)
        if res[0] < 2:
            return False
        while res[0] > 2:
            if res[0] % 2 == 0:
                res[0] = res[0] // 2
            else:
                break
        for i in range(1, len(res)):
            if res[i] % res[0] != 0:
                return False
        return True

if __name__ == "__main__":
    sol = Solution()
    testdata = [0,0,0,1,1,1,2,2,2]
    print(sol.hasGroupsSizeX(testdata))