class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        dict1 = {}
        for i, num in enumerate(nums):
            dict1[num] = i
        for i in range(len(nums)):
            if target - nums[i] in dict1 and dict1[target - nums[i]] != i:
                return [i, dict1[target - nums[i]]]
         


if __name__ == "__main__":
    solution = Solution()
    testdata1 = [3,3]
    testdata2 = 6
    result = solution.twoSum(testdata1, testdata2)
    print(result)