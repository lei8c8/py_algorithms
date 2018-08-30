class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        if num == 1:
            return True
        for i in 2, 3, 5:
            while num % i == 0:
                num /= i
        return num == 1

if __name__ == "__main__":
    solution = Solution()
    print(solution.isUgly(14))
