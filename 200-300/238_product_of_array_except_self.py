class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = []
        res = [0] * len(nums)
        mem = 1
        for i in range(len(nums)):
            temp.append(mem)
            mem *= nums[i]
        mem = 1
        i = len(nums) - 1
        while i >= 0:
            res[i] = temp[i] * mem
            mem *= nums[i]
            i -= 1
        return res