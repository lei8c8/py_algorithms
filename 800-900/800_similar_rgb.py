class Solution:
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        return "#" + self.getColor(color[1:3]) + \
            self.getColor(color[3:5]) + self.getColor(color[5:7])
        
    def getColor(self, c):
        number = int(c, 16)
        r = number // 17
        m = number % 17
        if m > 8: 
            r += 1
        return hex(r)[-1] * 2
        