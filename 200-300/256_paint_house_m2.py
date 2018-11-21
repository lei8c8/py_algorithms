class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        red, blue, green = 0, 0, 0
        for redCur, blueCur, greenCur in costs:
            red, blue, green = min(blue, green) + redCur, min(red, green) + blueCur, min(red, blue) + greenCur
        return min([red, blue, green])


if __name__ == "__main__":
    s = Solution()
    data = [[17,2,17],[16,16,5],[14,3,19]]
    result = s.minCost(data)
    print(result)
            