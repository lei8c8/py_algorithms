class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            v = 0
            for j in range(0, i):
                if nums[i] > nums[j]: v = max(v, dp[j])
            dp[i] = v + 1
        return max(dp)