class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest, second, index = -float("inf"), -float("inf"), 0
        for i in range(len(nums)):
            if nums[i] > largest:
                second = largest
                largest = nums[i]
                index = i
            elif nums[i] > second:
                second = nums[i]
        if largest >= 2 * second:
            return index
        return -1

