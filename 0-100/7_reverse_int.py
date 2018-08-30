class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        negative = (x < 0)
        x = abs(x)
        str_x = str(x)
        str_x = str(x)[::-1]
        while True:
            if str_x[0] == '0':
                str_x = str_x[1:]
            else:
                break
        if negative:
            str_x = '-' + str_x
        int_x = int(str_x)
        if int_x > (2 ** 31 - 1) or int_x < (0 - 2 ** 31):
            return 0
        return eval(str_x)

if __name__ == '__main__':
    solution = Solution()
    test_data = -1563847412
    result = solution.reverse(test_data)
    print(result)
