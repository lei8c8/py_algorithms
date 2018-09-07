class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        list = []
        p12 = self.calculate(p1, p2)
        p13 = self.calculate(p1, p3)
        p14 = self.calculate(p1, p4)
        p23 = self.calculate(p2, p3)
        p24 = self.calculate(p2, p4)
        p34 = self.calculate(p3, p4)
        list.extend([p12, p13, p14, p23, p24, p34])
        list.sort()
        if list.count(list[0]) == 4 and list.count(list[-1]) == 2:
            return True
        return False


    def calculate(self, a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2