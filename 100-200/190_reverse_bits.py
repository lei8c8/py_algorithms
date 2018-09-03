class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        temp = bin(n)[2:]
        length = len(temp)
        missing_zero_number = 32 - length
        zeros = []
        for _ in range(missing_zero_number):
            zeros.append('0')
        temp = ''.join(zeros) + temp
        temp = temp[::-1]
        return int(temp, 2)

if __name__ == "__main__":
    solution = Solution()
    result = solution.reverseBits(43261596)
    print(result)