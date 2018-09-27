class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                return nums[i+1]
        return nums[0]
