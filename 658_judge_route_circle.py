from collections import Counter

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        myCounter = Counter(moves)
        if (myCounter['U'] - myCounter['D'] == 0) and (myCounter['R'] - myCounter['L'] == 0):
            return True
        else:
            return False

if __name__ == '__main__':
    solution = Solution()
    test1 = 'UD'
    test2 = 'LL'
    print(solution.judgeCircle(test1))
    print(solution.judgeCircle(test2))
        