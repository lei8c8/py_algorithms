class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        res = float('inf')
        left = 0
        sum = 0
        for right in range(len(nums)):
            sum += nums[right]
            while (sum >= s):
                res = min(res, right - left + 1)
                sum -= nums[left]
                left += 1
        if res == float('inf'):
            return 0
        return res
