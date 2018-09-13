class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return None
        nums = [x for x in set(nums)]
        nums.sort()
        if len(nums) < 3:
            return nums[-1]
        else: 
            return nums[-3]

if __name__ == "__main__":
    solution = Solution()
    testdata = [3,2,1]
    result = solution.thirdMax(testdata)
    print(result)