class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        lookup = {}
        sorted_nums = sorted(nums, reverse=True)
        for i, v in enumerate(sorted_nums): 
            lookup[v] = i + 1
        for i in range(len(nums)):
            if lookup[nums[i]] == 1:
                nums[i] = "Gold Medal"
            elif lookup[nums[i]] == 2:
                nums[i] = "Silver Medal"
            elif lookup[nums[i]] == 3:
                nums[i] = "Bronze Medal"
            else:
                nums[i] = str(lookup[nums[i]])
        return nums

if __name__ == "__main__":
    solution = Solution()
    testdata = [1,3,5,9,6,7]
    result = solution.findRelativeRanks(testdata)
    print(result)