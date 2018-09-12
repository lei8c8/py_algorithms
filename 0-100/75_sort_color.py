class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index_0, index_1 = 0, 0
        for i in range(len(nums)):
            value = nums[i]
            nums[i] = 2
            if value < 2:
                nums[index_1] = 1
                index_1 += 1
                if value < 1:
                    nums[index_0] = 0
                    index_0 += 1
        