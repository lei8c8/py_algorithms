class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 2 ** 31 - 1 or x < 0 - 2 ** 31 or x == 0:
            return 0
        neg = False
        if x < 0: 
            neg = True
        x = str(abs(x))
        x = list(x)
        while x[-1] == '0':
            x.pop()
        x = x[::-1]
        x = ''.join(x)
        x = int(x)
        if neg:
            x = 0 - x
        if x > 2 ** 31 - 1 or x < 0 - 2 ** 31 or x == 0:
            return 0
        return x
