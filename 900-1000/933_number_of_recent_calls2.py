class RecentCounter:

    def __init__(self):
        self.times = []
        self.last = 0
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.times.append(t)
        index = 0 
        if len(self.times) == 1:
            return 1
        for i in range(self.last, len(self.times)):
            if t - self.times[i] <= 3000:
                index = i
                break
        self.last = index
        return len(self.times) - self.last 
