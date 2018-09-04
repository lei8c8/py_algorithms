class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        for i in range(1, len(nums)):
            if i == 1:
                nums[i] = max(nums[i], nums[0])
            else:
                nums[i] = max(nums[i] + nums[i-2], nums[i-1])
        return nums[-1]
