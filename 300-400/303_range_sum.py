class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.items = nums
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.items[i:j+1])