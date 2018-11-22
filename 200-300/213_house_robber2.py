class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)
        def helper(start, stop, nums):
            n = nums[start:stop+1]
            dp = [0] * len(n)
            dp[0], dp[1] = n[0], max(n[0], n[1])
            for i in range(2, len(n)):
                dp[i] = max(dp[i-1], dp[i-2] + n[i])
            return dp[-1]
        return max(helper(0,len(nums) - 2, nums), helper(1, len(nums) - 1, nums))
        