class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        number = 0
        for i in range(L, R + 1):
            i_bits = bin(i).count('1')
            if self.isPrime(i_bits):
                number += 1
        return number

    def isPrime(self, n):
        if n == 1:
            return False
        elif n == 2:
            return True
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
                if count > 2:
                    return False
        return True

if __name__ == "__main__":
    solution = Solution()
    result = solution.countPrimeSetBits(10, 15)
    print(result)