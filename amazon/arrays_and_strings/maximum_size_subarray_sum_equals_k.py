class Solution:
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total, res = 0, 0
        rangeSum = {0: -1}
        for i in range(len(nums)):
            total += nums[i]
            if total not in rangeSum: rangeSum[total] = i
            if total - k in rangeSum: 
                res = max(res, i - rangeSum[total - k])
        return res