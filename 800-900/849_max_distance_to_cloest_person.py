class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        consequentZero, ans = 0, 0
        for s in seats:
            if s == 0:
                consequentZero += 1
                ans = max(ans, consequentZero)
            else: 
                consequentZero = 0
        ans = (ans + 1) // 2
        return max(ans, seats.index(1), seats[::-1].index(1))