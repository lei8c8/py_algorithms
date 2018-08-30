class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        abs_num = abs(num)
        res = ''
        while abs_num >= 0:
            res += str(abs_num % 7)
            abs_num = abs_num // 7
            if abs_num == 0:
                break
        if num >= 0:
            return res[::-1]
        else: 
            return '-' + res[::-1]

