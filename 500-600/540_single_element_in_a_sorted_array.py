class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0 
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                i += 2
            else:
                return nums[i]
        return nums[-1]   
            