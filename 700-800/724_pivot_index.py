class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        move_total = 0
        if not nums: return -1
        if total == nums[0]:
            return 0
        for i in range(len(nums) - 1):
            move_total += nums[i]
            if move_total == total - nums[i + 1] - move_total:
                return i + 1
        return -1
