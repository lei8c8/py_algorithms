class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maximum = total = nums[0]
        for element in nums[1:]:
            if total + element > element:
                total = total + element
            else:
                total = element
            if maximum < total:
                maximum = total

        return maximum

if __name__ == "__main__":
    test_data = [-2,1,-3,4,-1,2,1,-5,4]
    solution = Solution()
    print(solution.maxSubArray(test_data))