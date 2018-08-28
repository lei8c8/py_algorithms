class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        previous = nums[0]
        length = len(nums)
        i = 1
        while i < length:
            if nums[i] == previous:
                nums.pop(i)
                length -= 1
                continue
            else:
                previous = nums[i]
                i += 1
        return len(nums)

if __name__ == '__main__':
    solution = Solution()
    test_data = [0,0,1,1,1,2,2,3,3,4]
    result = solution.removeDuplicates(test_data)
    print(result)