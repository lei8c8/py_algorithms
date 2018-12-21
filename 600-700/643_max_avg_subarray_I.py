class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        res, i, summ = sum(nums[:k]), 1, sum(nums[:k])
        while i <= len(nums) - k:
            summ = summ - nums[i-1] + nums[i+k-1]
            res = max(res, summ)
            i += 1
        return res / k