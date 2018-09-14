import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original = nums
        self.now = list(nums)
        self.n = len(nums)
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.now = list(self.original)
        return self.now
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(self.n):
            idx = random.randint(i,self.n-1)
            self.now[i], self.now[idx] = self.now[idx], self.now[i]
        return self.now
        