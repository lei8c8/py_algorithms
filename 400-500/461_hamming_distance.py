class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bits = bin(x ^ y)[2:]
        return bits.count('1')

if __name__ == '__main__':
    solution = Solution()
    test = solution.hammingDistance(1, 4)
    print(test)