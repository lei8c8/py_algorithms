class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list_len = len(nums)
        duplicated_item = sum(nums) - sum(set(nums))
        missing_item = list_len * (list_len + 1) // 2 - sum(set(nums))
        return [duplicated_item, missing_item]
