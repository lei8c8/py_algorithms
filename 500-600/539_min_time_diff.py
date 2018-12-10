class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        min_val = float('inf')
        for i in range(len(timePoints)):
            v = self.convertTimeToInt(timePoints[i])
            timePoints[i] = v 
        timePoints.sort()
        for i in range(1, len(timePoints)):
            min_val = min(min_val,(timePoints[i] - timePoints[i-1]))
        min_val = min(min_val, 1440 + timePoints[0] - timePoints[-1])
        if min_val > 1440: min_val = 1440 - min_val
        return min_val

    
    def convertTimeToInt(self, str):
        h, m = str.split(':')
        h, m = int(h), int(m)
        return h * 60 + m