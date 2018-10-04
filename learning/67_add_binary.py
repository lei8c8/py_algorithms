class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a, len_b = len(a), len(b)
        num_a, num_b = 0, 0
        for i in range(len_a):
            if a[i] == '1':
                num_a +=  2 ** (len_a - i -1)
        for i in range(len_b):
            if b[i] == '1':
                num_b += 2 ** (len_b - i - 1)
        num = num_a + num_b
        return bin(num)[2:]
