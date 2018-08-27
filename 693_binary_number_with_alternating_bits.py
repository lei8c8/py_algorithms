class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        my_list = list(bin(n)[2:])
        while len(my_list) >= 2:
            pop_element = int(my_list.pop())
            if pop_element ^ int(my_list[-1]) != 1:
                return False
        return True

if __name__ == '__main__':
    solution = Solution()
    print(solution.hasAlternatingBits(4))