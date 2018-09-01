class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num_str = [str(i) for i in digits]
        str_num = ''.join(num_str)
        num = int(str_num) + 1
        str_num = str(num)
        return [int(i) for i in str_num]