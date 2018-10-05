class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums[0], nums[1])
        left = 0 
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[left]:
                left = mid + 1
            else:
                right = mid
  
        return nums[left - 2]


if __name__ == "__main__":
    solution = Solution()
    testdata = [3,4,5,1,2]
    result = solution.findMin(testdata)
    print(result)