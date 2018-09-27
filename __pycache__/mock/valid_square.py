
class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        p1p2 = self.calculate(p1, p2)
        p1p3 = self.calculate(p1, p3)
        p1p4 = self.calculate(p1, p4)
        p2p3 = self.calculate(p2, p3)
        p2p4 = self.calculate(p2, p4)
        p3p4 = self.calculate(p3, p4)
        pe = [p1p2, p1p3, p1p4, p2p3, p2p4, p3p4]
        pe.sort()
        if pe[0] == 0:
            return False
        if pe[0] == pe[3] and pe[-1] == pe[-2]:
            return True
        return False
        

    
    def calculate(self, point1, point2):
        return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2