class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        total = duration
        for i in range(1, len(timeSeries)):
            if timeSeries[i] - timeSeries[i-1] >= duration:
                total += duration
            else:
                total += (timeSeries[i] - timeSeries[i-1] )
        return total