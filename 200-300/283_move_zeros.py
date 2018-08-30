class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        none_zero_number = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[none_zero_number] = nums[i]
                none_zero_number += 1
        for j in range(len(nums) - none_zero_number):
            nums[none_zero_number + j] = 0