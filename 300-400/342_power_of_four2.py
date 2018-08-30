class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        bin_num = bin(num)[2:]
        # if bin_num[0] == '1' and bin_num.count('0') == len(bin_num) - 1 and bin_num.count('0') % 2 == 0:
        #     return True
        # return False
        return True if bin_num[0] == '1' and bin_num.count('0') == len(bin_num) - 1 and bin_num.count('0') % 2 == 0 else False
