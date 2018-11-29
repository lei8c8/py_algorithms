class Solution:
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        distance = 0
        minVal, maxVal = arrays[0][0], arrays[0][-1]
        for i in range(1, len(arrays)):
            distance = max(abs(arrays[i][-1] - minVal), abs(maxVal - arrays[i][0]), distance)
            minVal = min(minVal, arrays[i][0])
            maxVal = max(maxVal, arrays[i][-1])
        return distance
        
        