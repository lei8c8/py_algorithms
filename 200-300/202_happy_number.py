class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        remember_me = set()
        while True:
            n = self.getHappy(n)
            if n == 1:
                return True
            if n in remember_me:
                return False
            else:
                remember_me.add(n)



    def getHappy(self, num):
        sum = 0
        while num >= 10:
            remaider = num % 10
            sum += remaider ** 2
            num = num // 10
        sum +=  num ** 2

        return sum
