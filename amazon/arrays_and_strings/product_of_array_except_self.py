class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        productUntilIndex, product = [], 1
        res = [None] * len(nums)
        for i in range(len(nums)):
            productUntilIndex.append(product)
            product *= nums[i]
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = productUntilIndex[i] * product
            product *= nums[i]
        return res
