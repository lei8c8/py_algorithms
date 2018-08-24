class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        temp = ['1' if n == '0' else '0' for n in bin(num)[2:] ]
        return int(''.join(temp), 2)



if __name__ == '__main__':
    solution = Solution()
    result = solution.findComplement(5)
    print(result)