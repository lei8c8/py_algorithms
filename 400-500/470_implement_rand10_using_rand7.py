# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
import random
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        i = 0
        while True:
            row = rand7()
            col = rand7()
            i = col + (row - 1) * 7
            if i <= 40:
                break
        return 1 + (i - 1) % 10 
