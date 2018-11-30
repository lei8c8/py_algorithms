class Solution:
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        res = [None] * len(nums)
        if a == 0 and b >=0:
            return [b * x + c for x in nums]
        if a == 0 and b < 0:
            return ([b * x + c for x in nums])[::-1]
        pivot = (b / 2 / a) * (-1)
        left, right, tail = 0, len(nums) - 1, len(nums) - 1
        while left <= right:
            if abs(nums[left] - pivot) > abs(nums[right] - pivot):
                res[tail] = a * nums[left] ** 2 + b * nums[left] + c 
                left += 1
            else:
                res[tail] = a * nums[right] ** 2 + b * nums[right] + c 
                right -= 1
            tail -= 1
        if a > 0: return res
        return res[::-1]
    