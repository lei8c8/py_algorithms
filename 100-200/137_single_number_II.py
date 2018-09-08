class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x, y = 0, 0
        for element in nums:
            y = y ^ element & ~x
            x = x ^ element & ~y
        return y