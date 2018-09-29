class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        S=0
        for i in range(len(points)):
            s=0
            D=dict()
            for j in range(len(points)):
                d=(points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2
                if d in D and d!=0:
                    D[d]+=1
                else:
                    D[d]=1
            for a in D.values():
                s+=a*(a-1)
            S+=s
        return S

if __name__ == "__main__":
    sol = Solution()
    testdata = [[0,0],[1,0],[2,0]]
    result = sol.numberOfBoomerangs(testdata)
    print(result)