class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        distance = 0
        found = 0
        bin_N = bin(N)[2:]
        for i in range(len(bin_N)):
            if bin_N[i] == '1':
                found += 1
                if found == 1:
                    current = last = i
                else:
                    current = i
                    if current - last > distance:
                        distance = current - last
            last = current
        return distance

if __name__ == '__main__':
    solution = Solution()
    print(solution.binaryGap(6))

